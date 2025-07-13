
tasks = []
def show_menu():
    print("\n======TO-DO LIST MENU======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not tasks:
        print("There is no tasks in the list.")
    else:
        tick = "\u2714"
        cross = "\u274C"
        for i, task in enumerate(tasks): status = tick + "Done" if  task["done"] else cross + "Not Done"
        print(f"{i + 1}.{task['task']} [{status}]")


def add_tasks():
    task_name = input("Enter the task:")
    tasks.append({"task": task_name,"done": False})
    print("Task added successfully! ")

def mark_done():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("Task marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted task:{removed['tasks']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

while True:
    show_menu()
    choice = input("Choose(1-5): ")
    if choice =='1':
        view_tasks()
    elif choice == '2':
        add_tasks()
    elif choice =='3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice =='5':
        print("Exiting.....")
        break
    else:
        print("Invalid choice")