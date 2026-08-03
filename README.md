# Todo App

A simple command-line todo app written in Python. Tasks are stored in a local
`tasks.json` file, so your list persists between runs.

Each task has a title, a done status (defaults to `False`), and a priority
(defaults to `medium`).

## Project structure

- `task.py` - the `Task` class
- `storage.py` - functions to save/load tasks to/from `tasks.json`
- `main.py` - the command-line interface
- `test_task.py` - pytest tests for the `Task` class

## Usage

### Add a task

```
python main.py add "Buy milk"
python main.py add "Write report" --priority high
```

### List tasks

```
python main.py list
```

```
0: [ ] Buy milk (priority: medium)
1: [ ] Write report (priority: high)
```

### Mark a task as done

```
python main.py done 0
```

### Edit a task's title

```
python main.py edit 1 "Write final report"
```

### Delete a task

```
python main.py delete 0
```

Commands that take an `<index>` refer to the number shown by `list`. Invalid
input (non-numeric or out-of-range indexes) is handled gracefully and prints
a friendly error instead of crashing.

## Running tests

```
python -m pytest
```

## Credits

Built with [Claude Code](https://claude.com/claude-code).
