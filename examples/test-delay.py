import os
from dotenv import load_dotenv
from clarity import Clarity
import time
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
session_id = client.create_session("test_session_via_test_py") # Use a distinct name for testing

start_time = time.time()
# Get completion using the client
completion_response = client.complete(session_id, prompt, agent_name, parse_json=True) # Pass agent_name
# print("\nCompletion JSON:")
print(completion_response["json"])
end_time = time.time()
response_time = end_time - start_time
print(f"\nResponse time: {response_time:.2f} seconds")

time.sleep(60)
# Get completion using the client
start_time = time.time()
completion_response = client.complete(session_id, prompt, agent_name, parse_json=True) # Pass agent_name
end_time = time.time()
response_time = end_time - start_time
# print("\nCompletion JSON:")
print(completion_response["json"])
print(f"\nResponse time: {response_time:.2f} seconds")

time.sleep(600)

# Get completion using the client and measure response time
start_time = time.time()
completion_response = client.complete(session_id, "I want paintings of professors who discovered fossils", agent_name, parse_json=True) # Pass agent_name
end_time = time.time()
response_time = end_time - start_time
# print("\nCompletion JSON:")
print(completion_response["json"])
print(f"\nResponse time: {response_time:.2f} seconds")
    
