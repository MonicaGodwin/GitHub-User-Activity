def handle_push():
    return "A commit was pushed"

def handle_create():
    return "A repository was created"

def handle_fork():
    return "A repository was forked"

def handle_watch():
    return "Starred a repository"

def handle_issues():
    return "Updated an issue"

def handle_delete():
    return "Deleted a branch"


event_type = {
    "PushEvent": handle_push,
    "CreateEvent": handle_create,
    "ForkEvent": handle_fork,
    "WatchEvent": handle_watch,
    "IssuesEvent": handle_issues,
    "DeleteEvent": handle_delete
}
