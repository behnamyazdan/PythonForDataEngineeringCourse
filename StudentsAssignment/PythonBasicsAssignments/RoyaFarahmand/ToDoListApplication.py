
# ToDo List

todo_list = []


def add_task():
    task = input("\nEnter task: ")
    todo_list.append(task)
    print("\nTask added successfully!")


def view_tasks():
    if not todo_list:
        print("\nNo tasks here yet!")
    else:
        for task in todo_list:
            print(task)


def task_done(task):
    if task in todo_list:
        todo_list.remove(task)
        print("\nGood Job!")
    else:
        print("\nTask not found!")


def delete_task(task):
    if task in todo_list:
        todo_list.remove(task)
        print("\nTask removed!")
    else:
        print("\nTask not found!")


while True:
    print("\n1. Add New Task")
    print("2. View All Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task = input('Which task is done? ')
        task_done(task)
    elif choice == "4":
        task = input('Which task do you want to remove? ')
        delete_task(task)
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("\nInvalid choice! Please enter a number between 1 and 5.")
