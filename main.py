import sys
from urllib.request import urlopen
from urllib.request import HTTPError, URLError
import json
import os
from helper_function import event_type

if len(sys.argv) < 2:
    print("Usage: [main.py] [username]")
    sys.exit()
elif len(sys.argv) > 2:
    print("Error: Please provide only one username")
    sys.exit()

user_input = sys.argv[1]

url = f"https://api.github.com/users/{user_input}/events"

try:
    response = urlopen(url)
except HTTPError as e:
    print(f"HTTP error {e.code}: {e.reason}")
    sys.exit()
except URLError as e:
    print(f"Request failed: {e.reason}")
    sys.exit()

raw_data = response.read()

raw_data = raw_data.decode()

try:
    converted_data = json.loads(raw_data)
except json.JSONDecodeError:
  print("The JSON file is empty or formatted incorrectly.")
  sys.exit()

content_file = []   
if not os.path.exists("file.json"):        
    with open("file.json", "w") as file:
        json.dump(content_file, file, indent=4)
else:
    with open("file.json", "r") as data:
        file_content = json.load(data)

for converted in converted_data:
    repo = converted["repo"]["name"]
    time = converted["created_at"]
    current_event = converted["type"]

    handler = event_type.get(current_event)
    if handler:
        description = handler()
    else:
        print("Unknown Event")
    print(description)

    content = {
        "type": current_event,
        "repo": repo,
        "created_at": time
    }

    content_file.append(content)
    print(f"{content["type"]} to {content["repo"]}\n{content['created_at']}\n")

with open("file.json", "w") as data_file:
    json.dump(content_file, data_file, indent=4)

