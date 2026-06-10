from task_manager.task_utils import (
    add_task,
    mark_task_as_complete,
    view_pending_tasks,
    calculate_progress
)

from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)


def main():
    tasks = []

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Track Progress")
        print("5. Exit")

        choice = input("Choose option: ")

        # ➕ ADD TASK
        if choice == "1":
            try:
                title = validate_task_title(input("Title: "))
                description = validate_task_description(input("Description: "))
                due_date = validate_due_date(input("Due Date (YYYY-MM-DD): "))

                add_task(tasks, title, description, due_date)
                print("Task added successfully!")

            except ValueError as e:
                print(e)

        # ✅ COMPLETE TASK
        elif choice == "2":
            title = input("Enter title to mark complete: ")
            mark_task_as_complete(tasks, title)
            print("Task marked as complete!")

        # 📋 PENDING TASKS
        elif choice == "3":
            pending = view_pending_tasks(tasks)

            if len(pending) == 0:
                print("No pending tasks.")
            else:
                print("\nPending Tasks:")
                for task in pending:
                    print(f"- {task['title']} (Due: {task['due_date']})")

        # 📊 PROGRESS
        elif choice == "4":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress:.2f}%")

        # 🚪 EXIT
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()