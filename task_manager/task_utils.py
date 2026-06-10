from task_manager.validation import (
    validate_task_title,
    validate_task_description,
    validate_due_date
)

# ➕ ADD TASK
def add_task(tasks, title, description, due_date):
    task = {
        "title": validate_task_title(title),
        "description": validate_task_description(description),
        "due_date": validate_due_date(due_date),
        "completed": False
    }

    tasks.append(task)
    return tasks


# ✅ MARK COMPLETE
def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"] == title:
            task["completed"] = True
            return tasks
    return tasks


# 📋 VIEW PENDING TASKS
def view_pending_tasks(tasks):
    return [task for task in tasks if task["completed"] is False]


# 📊 CALCULATE PROGRESS
def calculate_progress(tasks):
    if len(tasks) == 0:
        return 0

    completed = sum(1 for task in tasks if task["completed"])
    return (completed / len(tasks)) * 100