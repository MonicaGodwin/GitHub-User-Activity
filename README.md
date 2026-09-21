# GitHub User Activity

A simple command-line interface (CLI) built with Python's standard library for fetching and displaying a GitHub user's recent activity.

## Requirements

* Python 3
* No external libraries

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MonicaGodwin/GitHub-User-Activity.git
```

### 2. Navigate into the project directory

```bash
cd GitHub-User-Activity
```

## Usage

Run the program using:

```bash
python3 main.py <github_username>
```

For example:

```bash
python3 main.py piusjohn
```

The program fetches the user's recent GitHub activity and displays information such as:

* Event type
* Repository name
* Date and time of the activity

## User Data

The fetched and converted user activity is stored in `file.json`.

Each activity is represented as a JSON object containing:

```json
{
    "type": "PushEvent",
    "repo": {
        "name": "username/repo"
    },
    "created_at": "2026-09-20T12:30:00Z"
}
```

The `type` represents the GitHub event, `repo.name` represents the repository where the activity occurred, and `created_at` represents when the activity happened.

## Supported Activities

The CLI converts GitHub event types into human-readable descriptions, including:

* `PushEvent` → Pushed commits
* `CreateEvent` → Created a repository
* `WatchEvent` → Starred a repository
* `IssuesEvent` → Updated an issue
* `ForkEvent` → Forked a repository
* `DeleteEvent` → Deleted a branch

## Project Structure

```text
github-user-activity/
│
├── file.json
├── main.py
└── README.md
```

## Project Page

This project was built as part of the roadmap.sh GitHub User Activity project:

https://roadmap.sh/projects/github-user-activity

## License

This project is open source and available for learning and personal use.
