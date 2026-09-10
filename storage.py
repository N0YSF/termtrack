import json
from pathlib import Path


DATA_FILE = Path("data/tasks.json")


def _load_tasks():
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def _save_tasks(tasks):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def add_task(title):
    tasks = _load_tasks()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    _save_tasks(tasks)

    return task


def list_tasks():
    return _load_tasks()


def complete_task(task_id):
    tasks = _load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            _save_tasks(tasks)
            return True

    return False
