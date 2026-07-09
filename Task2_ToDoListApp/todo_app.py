import sys


def display_progress_bar(completed, total):
    """Calculates completion percentage and renders a clean CLI progress bar."""
    if total == 0:
        percent = 0
        bar = "░" * 20
    else:
        percent = int((completed / total) * 100)
        completed_blocks = int((completed / total) * 20)
        remaining_blocks = 20 - completed_blocks
        bar = "█" * completed_blocks + "░" * remaining_blocks

    print(f"\nProgress: [{bar}] {percent}% ({completed}/{total} tasks completed)")


def view_tasks(tasks):
    """Displays the current list of tasks with their completion status."""
    print("\n" + "=" * 40)
    print("             CURRENT TASKS             ")
    print("=" * 40)

    if not tasks:
        print(" No tasks found. Add some to get started!")
        print("-" * 40)
        display_progress_bar(0, 0)
        return

    completed_count = 0
    for idx, task in enumerate(tasks, start=1):
        status = "[Done]" if task["completed"] else "[Pending]"
        if task["completed"]:
            completed_count += 1
        print(f"{idx}. {task['title']:<25} {status}")

    print("-" * 40)
    display_progress_bar(completed_count, len(tasks))


def main():
    tasks = []

    while True:
        print("\n" + "═" * 40)
        print("        TO-DO LIST MANAGER UI        ")
        print("═" * 40)
        print("1. View Tasks & Progress")
        print("2. Add New Task")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit Application")
        print("═" * 40)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            title = input("\nEnter the task description: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                print(f"Success: '{title}' added to your list.")
            else:
                print("Error: Task description cannot be empty!")

        elif choice == "3":
            view_tasks(tasks)
            if not tasks:
                continue
            try:
                task_num = int(input("\nEnter task number to mark complete: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print(
                        f"Marked task #{task_num} as completed!"
                    )
                else:
                    print("Error: Invalid task number.")
            except ValueError:
                print("Error: Please enter a valid numerical digit.")

        elif choice == "4":
            view_tasks(tasks)
            if not tasks:
                continue
            try:
                task_num = int(input("\nEnter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed task: '{removed['title']}'")
                else:
                    print("Error: Invalid task number.")
            except ValueError:
                print("Error: Please enter a valid numerical digit.")

        elif choice == "5":
            print("\nExiting To-Do List Application. Have a productive day!")
            break
        else:
            print("⚠ Error: Invalid option selected. Please choose between 1-5.")


if __name__ == "__main__":
    main()