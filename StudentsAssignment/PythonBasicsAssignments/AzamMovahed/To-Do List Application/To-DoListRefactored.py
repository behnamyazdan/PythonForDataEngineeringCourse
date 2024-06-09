
STATUS = ('Created', 'In_progress', 'Pause', 'Cancel', 'Done')
agenda = {}


def print_agenda(dic_name):
    if not dic_name:
        print('Todo list is empty. Let\'s create your todolist')
    else:
        for k, v in dic_name.items():
            print(f"{k}: {v}")


def add_task(dic_name, input_str):
    for item in input_str:
        dic_name[item] = STATUS[0]


def remove_task(dic_name, input_name):
    try:
        dic_name = {k: v for k, v in dic_name.items() if k != input_name}
        return dic_name
    except ValueError:
        print('Invalid entry. Please enter correct task.')


def edit_task_state(dic_name, dic_task, state_num):
    if {k: v for k, v in dic_name.items() if k == dic_task}:
        dic_name[dic_task] = STATUS[state_num - 1]
    else:
        print('Invalid entry. Please enter correct task and state.')


print('\nWelcome to Sahar_MVD Todolist Editor. You have 5 options.')
print('1-See your agenda\n2-Add task\n3-Remove task\n4-Edit state of task\n5-Exit')

while True:
    try:
        user_selection = int(input('Enter the number of the option : '))
        if user_selection == 1:
            print_agenda(agenda)
        elif user_selection == 2:
            task_name = input('Enter tasks and separate them with dash for multiple entry: ').split('-')
            add_task(agenda, task_name)
            print_agenda(agenda)
        elif user_selection == 3:
            task_name = input('Enter the task name to delete: ')
            agenda = remove_task(agenda, task_name)
            print_agenda(agenda)
        elif user_selection == 4:
            print('You can change the state of your task:')
            for i, s in enumerate(STATUS):
                print(i + 1, s)
            task = input('Enter the name of the task for changing state: ')
            state = int(input('Enter the number of the state: '))
            edit_task_state(agenda, task, state)
            print_agenda(agenda)
        elif user_selection == 5:
            print('Stick to your plan.bye!')
            break
        else:
            print('Invalid option. Please choose a valid option.')
    except ValueError:
        print('Invalid entry. Please enter a number.')

