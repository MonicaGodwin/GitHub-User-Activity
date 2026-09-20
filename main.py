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

data = json.loads(raw_data)

data = data.decode()

if not os.path.exists("file.json"):
    content = []
    with open("file.json", "w") as file:
        json.dump(content, file, indent=4)
else:
    with open("file.json", "r") as data:
        file_content = json.loads(data)
