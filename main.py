import argparse

from task import Task
from storage import load_tasks, save_tasks

def cmd_add(args):
    tasks = load_tasks()

    title = args.title.strip()
    if not title:
        print("Error: task title cannot be empty.")
        return

    title = args.title.strip()
    tasks.append(Task(title=title, priority=args.priority))
    save_tasks(tasks)
    print(f"Added task: {title} (priority: {args.priority})")


def cmd_list(args):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks):
        status = "x" if task.done else " "
        print(f"{index}: [{status}] {task.title} (priority: {task.priority})")


def cmd_done(args):
    tasks = load_tasks()
    try:
        tasks[args.index].mark_done()
    except (IndexError, TypeError):
        print(f"Error: no task at index {args.index}.")
        return
    save_tasks(tasks)
    print(f"Marked task {args.index} as done.")


def cmd_delete(args):
    tasks = load_tasks()
    try:
        removed = tasks.pop(args.index)
    except (IndexError, TypeError):
        print(f"Error: no task at index {args.index}.")
        return
    save_tasks(tasks)
    print(f"Deleted task: {removed.title}")


def cmd_edit(args):
    tasks = load_tasks()
    try:
        task = tasks[args.index]
    except (IndexError, TypeError):
        print(f"Error: no task at index {args.index}.")
        return
    old_title = task.title
    task.title = args.new_title
    save_tasks(tasks)
    print(f"Renamed task {args.index}: '{old_title}' -> '{args.new_title}'")


def parse_index(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def build_parser():
    parser = argparse.ArgumentParser(description="A simple command-line todo app.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")
    add_parser.add_argument(
        "--priority", default="medium", help="Priority of the task (default: medium)"
    )
    add_parser.set_defaults(func=cmd_add)

    list_parser = subparsers.add_parser("list", help="Show all tasks")
    list_parser.set_defaults(func=cmd_list)

    done_parser = subparsers.add_parser("done", help="Mark a task as complete")
    done_parser.add_argument("index", help="Index of the task")
    done_parser.set_defaults(func=cmd_done)

    delete_parser = subparsers.add_parser("delete", help="Remove a task")
    delete_parser.add_argument("index", help="Index of the task")
    delete_parser.set_defaults(func=cmd_delete)

    edit_parser = subparsers.add_parser("edit", help="Change a task's title")
    edit_parser.add_argument("index", help="Index of the task")
    edit_parser.add_argument("new_title", help="New title for the task")
    edit_parser.set_defaults(func=cmd_edit)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "index"):
        index = parse_index(args.index)
        if index is None:
            print(f"Error: '{args.index}' is not a valid index. Please enter a number.")
            return
        args.index = index

    args.func(args)


if __name__ == "__main__":
    main()
