tasks = []
def add_tasks(task_name: str) -> list:
    """
    Add a new task to the list of tasks.

    Args:
        task_description (str): Description of the task to be added.
    """
    tasks.append({"task_name": task_name, "completed": False})
    print("Task added!")

def mark_completed(task_index: int) -> None:
    """
    Mark a task as completed.

    Args:
        task_index (int): Index of the task to be marked as completed.
    """
    if task_index >= 0 and task_index < len(tasks):
        if tasks[task_index]["completed"]:
            print("Task is already completed")
        else:
            tasks[task_index]["completed"] = True
            print("Task is marked as completed")
    else:
        print("You have entered an invalid index")