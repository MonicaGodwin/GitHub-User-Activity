import sys
from urllib.request import urlopen
import json
import os

if len(sys.argv) < 2:
    print("Usage: [main.py] [username]")
    sys.exit()
elif len(sys.argv) > 2:
    print("Error: Please provide only one username")
    sys.exit()

user_input = sys.argv[1]
url = f"https://api.github.com/users/{user_input}/events"
response = urlopen(url)
raw_data = response.read()
raw_data = raw_data.decode()
converted_data = json.loads(raw_data)

content_file = []   
if not os.path.exists("file.json"):        
    with open("file.json", "w") as file:
        json.dump(content_file, file, indent=4)
else:
    with open("file.json", "r") as data:
        file_content = json.load(data)

for converted in converted_data:
    description = ""
    event_type = converted["type"]
    if event_type == "PushEvent":
        description = "Pushed commit"
    elif event_type == "CreateEvent":
        description = "Created a repository"
    elif event_type == "WatchEvent":
        description = "Starred a repository"
    elif event_type == "IssuesEvent":
        description = "updated an issue"
    elif event_type == "ForkEvent":
        description = "Forked a repository"
    elif event_type == "DeleteEvent":
        description = "Deleted a branch"
    else:
        description = "Unknown event"
    repo = converted["repo"]["name"]
    time = converted["created_at"]

    content = {
        "type": event_type,
        "description": description,
        "repo": repo,
        "created_at": time
    }
    content_file.append(content)
    print(f"{content["description"]} to {content["repo"]}\n{content['created_at']}\n")

with open("file.json", "w") as data_file:
    json.dump(content_file, data_file, indent=4)
