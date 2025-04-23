# clarity-api

A simple Python package for working with Yale's Clarity API.


## Install

```bash
pip install git+https://github.com/project-lux/clarity-api.git
```

## Example .env

```bash
CLARITY_URL=your_clarity_url
CLARITY_INSTANCE_ID=your_clarity_instance_id
CLARITY_AGENT_NAME=your_clarity_agent
CLARITY_API_KEY=your_clarity_key
```

## Example Usage

```python
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
session_id = client.create_session("test_session_via_test_py") # Use a distinct name for testing

# Get completion using the client
completion_response = client.complete(session_id, prompt, agent_name, parse_json=True) # Pass agent_name

# print("\nCompletion JSON:")
print(completion_response["json"])

print("\nContent:")
print(completion_response["content"])
```python