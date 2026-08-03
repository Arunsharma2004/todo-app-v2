import json
import os

from task import Task

DEFAULT_FILE = "tasks.json"


def save_tasks(tasks, filename=DEFAULT_FILE):
    with open(filename, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)


def load_tasks(filename=DEFAULT_FILE):
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return []

    return [Task.from_dict(item) for item in data]
