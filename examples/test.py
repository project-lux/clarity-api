import os
from dotenv import load_dotenv
from clarity import Clarity

load_dotenv()  # Load environment variables from .env file

# Get configuration from environment variables
base_url = os.getenv("CLARITY_URL")
instance_id = os.getenv("CLARITY_INSTANCE_ID")
agent_name = os.getenv("CLARITY_AGENT_NAME")
api_key = os.getenv("CLARITY_API_KEY")


# Instantiate the Clarity client
client = Clarity(base_url=base_url, instance_id=instance_id, api_key=api_key)

# Define a sample prompt
prompt = "I want paintings of professors who discovered fossils"

# Create a session using the client
session1 = client.create_session("test1") # Use a distinct name for testing
print("Session ID: ", session1.session_id)
print(client.sessions)

session2 = client.create_session("test2") # Use a distinct name for testing
print("Session ID: ", session2.session_id)
print(client.sessions)

# Get completion using the client
completion_response = client.complete(session1, prompt, agent_name, parse_json=True)
# print("\nCompletion JSON:")
print(completion_response["json"])



# print("\nContent:")
# print(completion_response["content"])
