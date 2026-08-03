from task import Task


def test_create_task_defaults():
    task = Task(title="Buy milk")
    assert task.title == "Buy milk"
    assert task.done is False
    assert task.priority == "medium"


def test_create_task_with_custom_priority_and_done():
    task = Task(title="Ship release", done=True, priority="high")
    assert task.title == "Ship release"
    assert task.done is True
    assert task.priority == "high"


def test_mark_done():
    task = Task(title="Write tests")
    assert task.done is False
    task.mark_done()
    assert task.done is True


def test_to_dict():
    task = Task(title="Clean house", done=True, priority="low")
    assert task.to_dict() == {
        "title": "Clean house",
        "done": True,
        "priority": "low",
    }


def test_from_dict():
    data = {"title": "Read book", "done": True, "priority": "high"}
    task = Task.from_dict(data)
    assert task.title == "Read book"
    assert task.done is True
    assert task.priority == "high"


def test_from_dict_with_missing_optional_fields():
    data = {"title": "Water plants"}
    task = Task.from_dict(data)
    assert task.title == "Water plants"
    assert task.done is False
    assert task.priority == "medium"


def test_round_trip_to_dict_from_dict():
    original = Task(title="Pay bills", done=True, priority="high")
    restored = Task.from_dict(original.to_dict())
    assert restored.title == original.title
    assert restored.done == original.done
    assert restored.priority == original.priority
