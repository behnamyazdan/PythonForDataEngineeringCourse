
agenda = []
status = ('In_progress', 'Pause', 'Cancel', 'Done')
user_selection = 0

# print flatlist or nestedlist


def print_list(list_name):
    if len(list_name) == 0:
        print('todo list is empty.lets creat your todolist')
    else:
        for x in list_name:
            if type(x) == list:
                for y in x:
                    print(y, end=' ')
                print()
            else:
                print(x)


# print_list(todo_list)


print(' \n Welcome to Sahar_MVD Todolist Editor. \n you have 5 option.')
print('   1-See your agenda \n   2-Add task \n   3-Remove task \n   4-edit state of task \n   5-exit')


while user_selection != 5:
    #try:
    user_selection = int(input('Enter number of option that you want:'))
    #except ValueError:
     #  print('invalid entry')
    if user_selection == 1:
        print_list(agenda)
    elif user_selection == 2:
        task_name = (input('enter name of task: '))
        agenda.append((task_name.split()))
    # nested_list.append(str1.split())
        print_list(agenda)
    elif user_selection == 3:
        task_name = (input('enter task name for delete: '))
        for item in agenda:
            #for element in item:
                #if element == task_name:
            if agenda[agenda.index(item)][0] == task_name:
                agenda.remove(item)
                print_list(agenda)

    elif user_selection == 4:
        print('you can change state of your task:')
        for i in status:
            print(status.index(i), i)
        task = str(input('enter name of task for changing state: '))
        state = int(input('enter number of state: '))
        for row in agenda:
            for element in row:
                if element == task:
                    if len(row) > 1:
                        row[1] = status[state]
                        print_list(agenda)
                    else:
                        row.append(status[state])
                        print_list(agenda)
                else:
                    break
if user_selection == 5:
    print('stick to your plan.bye!')







