import json
from handler import resize_handler

with open("test-event.json") as f:
    event = json.load(f)

# Lambda context can be None for local testing
response = resize_handler(event, None)
print(response)