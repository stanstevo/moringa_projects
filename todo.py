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

def show_menu():
    '''
    Display a welcome message and a list of available actions.
    
    Args:
        None

    Returns:
        None
    
    Raises:
        None
    
    Note:
        Use the print() function to display the message.
    
    '''
    print('Welcome to the to-do list manager')
    print('Please select an action\n "1. Add Task"\n "2. Mark Task as Completed"\n "3. List Tasks"\n "4. Remove Task"\n "5. Quit"\n')

def prompt():
    while True:
        show_menu()
        option = int(input("Enter your option: "))
        match option:
            case 1: 
                task_name = input("Enter task name: ")
                add_tasks(task_name)            
            case 2:
                index = int(input("Enter task index: "))
                mark_completed(index)
            case 3:
                list_tasks(tasks)
            case 4:
                index = int(input("Enter task index: "))
                remove_task(index)
            case 5:
                print("Goodbye!")
                break    
            case _:
                print("Invalid option")

def main():
    prompt()

if __name__ == "__main__":
    main()