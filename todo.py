tasks = []
def add_tasks(task_name: str) -> list:
    """
    Add a new task to the list of tasks.

    Args:
        task_description (str): Description of the task to be added.
    """
    tasks.append({"task_name": task_name, "completed": False})
    print("Task added!")