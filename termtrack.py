import argparse
from storage import add_task, list_tasks, complete_task


def main():
    parser = argparse.ArgumentParser(
        description="Simple terminal task tracker"
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    subparsers.add_parser("list")

    done_parser = subparsers.add_parser("done")
    done_parser.add_argument("task_id", type=int)

    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Added task #{task['id']}: {task['title']}")

    elif args.command == "list":
        tasks = list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "x" if task["completed"] else " "
            print(f"[{status}] {task['id']}: {task['title']}")

    elif args.command == "done":
        if complete_task(args.task_id):
            print(f"Completed task #{args.task_id}")
        else:
            print("Task not found.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
