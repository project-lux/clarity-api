import requests # Or httpx, http.client
import json # Import the json module

class Session:
    def __init__(self, session_id):
        self.session_id = session_id
        self.history = []

    def __str__(self):
        return self.session_id

    def add_history(self, entry):
        self.history.append(entry)


class Clarity:
    def __init__(self, base_url, instance_id, api_key, agent_name):
        self.base_url = f"{base_url}/instances/{instance_id}"
        self.instance_id = instance_id
        self.agent_name = agent_name
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "text/plain", # Add others as needed
            "X-AGENT-ACCESS-TOKEN": api_key
        }
        self.sessions = {}

    def _post(self, path, json_data):
        url = f"{self.base_url}{path}"
        # Replace with httpx.post or http.client logic if not using requests
        response = requests.post(url, headers=self.headers, json=json_data)
        response.raise_for_status() # Raise an exception for bad status codes
        return response.json()

    def create_session(self, session_name):
        response_body = self._post("/sessions", {"name": session_name})
        session = Session(response_body.get("sessionId"))
        self.sessions[session_name] = session
        return session

    def complete(self, prompt, session=None, parse_json=True):
            if session is None:
                session = list(self.sessions.values())[0]
            body = {
                "user_prompt": prompt,
                "agent_name": self.agent_name,
                "session_id": session.session_id
            }
            response_body = self._post("/completions", body)
            session.add_history({"prompt": prompt, "response": response_body})

            # Add the parsed JSON if requested and possible
            if parse_json:
                content_list = response_body.get("content")
                response_body["json"] = self.get_json(content_list[0].get("value"))
            return response_body

    def get_json(self, input_string):
        """Extracts and parses JSON from the 'value' of the first item in content_list."""
        try:
            return json.loads(input_string)
        except json.JSONDecodeError:
            # Look for JSON markdown format in content_value
            if "```json" in input_string:
                start = input_string.find("```json") + 7
                end = input_string.find("```", start)
            else:
                end = -1
            if end != -1:
                json_string = input_string[start:end].strip()
                try:
                    return json.loads(json_string)
                except json.JSONDecodeError:
                    # Handle cases where the string is not valid JSON
                    print(f"Warning: Could not decode JSON: {json_string[:100]}...")
                    return None
            else:
                print("None. Here's the string:")
                print(input_string)
                return None
