class Task:
    def __init__(self, title, done=False, priority="medium"):
        self.title = title
        self.done = done
        self.priority = priority

    def mark_done(self):
        self.done = True

    def to_dict(self):
        return {
            "title": self.title,
            "done": self.done,
            "priority": self.priority,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data["title"],
            done=data.get("done", False),
            priority=data.get("priority", "medium"),
        )

    def __repr__(self):
        status = "x" if self.done else " "
        return f"[{status}] {self.title} ({self.priority})"
