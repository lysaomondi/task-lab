from datetime import datetime

def validate_task_title(title):
    if not isinstance(title, str) or title.strip() == "":
        raise ValueError("Invalid title")
    return title.strip()


def validate_task_description(description):
    if not isinstance(description, str) or description.strip() == "":
        raise ValueError("Invalid description")
    return description.strip()


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Invalid due date")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid due date format")

    return due_date