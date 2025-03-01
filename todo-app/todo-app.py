def todo_app():
    tasks = []

    print('-------------Welcome to Todo App-----------------')
    total_tasks= int(input('Enter how many tasks you want to add : '))
    for i in range(1, total_tasks + 1):
        task_name = input(f'Enter your {i} task :  ')
        tasks.append(task_name)
    print(f'Today tasks are \n{tasks}')  
    while True:
        operation = int(input('1.add\n2.update\n3.delete\n4.view\n5.exit\n\n'))
        if operation == 1:
            add = input('Enter the task you want to add : ')
            tasks.append(add)
            print(f'\nyour task {add} has been added successfully...') 
        elif operation == 2:
            print('---------------------------------------')
            updated_task = input('Enter the task you want to add : ')
            if updated_task in tasks:
                print('---------------------------------------')
                new_task = input('Enter the new task : ')
                ind = tasks.index(updated_task)
                tasks[ind] = new_task
                print('---------------------------------------')
                print(f'{new_task} has been added Successfully')
                print('---------------------------------------')
                print(f'your updated tasks list are\n{tasks}')

        elif operation == 3:
            del_task = input('Enter the task you want to delete : ')
            if del_task in tasks:

                ind = tasks.index(del_task)
                del tasks[ind]
                print('----------------------------------------')
                print(f'Task {del_task} has been deleted successfully')
        
        elif operation == 4:
            print(f'Total tasks: {tasks}')
        
        elif operation == 5:
            print('-------Closing Todo-app...--------')
            break
        else:
            print('Please enter a valid number')    
print(todo_app())            