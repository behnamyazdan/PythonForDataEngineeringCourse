# create empty list for tasks
tasks=[]
print('Hello and welcome to TO DO LIST app')
while True:
    #menue options
    print()
    print('*** Main Menue ***')
    print('1 - Create a task')
    print('2 - View all tasks')
    print('3 - Mark a task as done')
    print('4 - delete tasks')
    print('5 - save tasks')
    print('6 - load tasks from a file')
    print('7 - Exit')

    # get option from user
    menue_inp = input('Please Choose a number: ')
    if menue_inp == '1':
        print('\nlets create a task!\n')
        while True:
            inp_option = input('press 1 to add a task or 0 to return to main menu: ')
            if inp_option == '1':
                new_task = input('type your task: ')
                tasks.append([new_task, 'not done'])
                print('task added successfully!')
                continue
            elif inp_option == '0':
                break
            else:
                print('invalid option')

    elif menue_inp =='2':
        print('\nlets view tasks\n')
        while True:
            inp_option = input('press 1 to view tasks or 0 to return to main menu: ')
            if inp_option == '1':
                for i, j in tasks:
                    indx = tasks.index([i, j])
                    print(indx + 1, '-', i, ', status:', j)
                continue
            elif inp_option == '0':
                break
            else:
                print('invalid option')

    elif menue_inp =='3':
        print('\nlets mark tasks as done\n')
        while True:
            print('Tasks:')
            indx_list= []
            for i, j in tasks:
                indx = tasks.index([i, j])
                indx_list.append(str(indx+1))
                print(indx + 1, '-', i, ', status:', j)
            inp_option = input('choose a task number to mark as done or press 0 to return to main menue: ')
            if inp_option in indx_list :
                tasks[int(inp_option)-1][1] = 'done'
                print(f'task {inp_option} marked as done successfully!')
                continue
            elif inp_option == '0':
                break
            else:
                print('invalid option')

    elif menue_inp =='4':
        print('\nlets delete tasks\n')
        while True:
            print('Tasks:')
            indx_list= []
            for i, j in tasks:
                indx = tasks.index([i, j])
                indx_list.append(str(indx+1))
                print(indx + 1, '-', i, ', status:', j)
            inp_option = input('choose a task number to delete or press 0 to return to main menue: ')
            if inp_option in indx_list :
                tasks.pop(int(inp_option)-1)
                print(f'task {inp_option} deleted successfully!')
                continue
            elif inp_option == '0':
                break
            else:
                print('invalid option')

    elif menue_inp =='5':
        print('\nthis section in not completed yet\n')
    elif menue_inp =='6':
        print('\nthis section in not completed yet\n')
    elif menue_inp =='7':
        print('\ngood bye!\n')
        break
    else:
        print('\ninvalid option\n')

