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

def list_tasks(tasks: list) -> None:
    """
    List all tasks.

    Args:
        tasks (list): List of tasks.
    """
    if len(tasks) == 0:
        print("No tasks to display")
    else:
        for task_number, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{task_number}. {task['task_name']} - {status}")

def remove_task(task_index: int) -> None:
    """
    Remove a task.

    Args:
        task_index (int): Index of the task to be removed.
    """
    if task_index >= 0 and task_index < len(tasks):
        tasks.pop(task_index)
        print("Task removed!")
    else:
        print("You have entered an invalid index")