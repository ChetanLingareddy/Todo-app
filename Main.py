
todos=[]
while True:
    user_action= input("Type add, show, edit or exit : ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input ("Enter a To-do : ")
            todos.append(todo)
        case 'show':
            for x in todos:
                print(x.capitalize())
        case 'edit':
            number  = int(input("enter a To-do list number to edit: "))
            new_number = number -1
            new_todo= input("enter your new To-do: ")
            todos[new_number]=new_todo
        case 'exit':
            break
print ('bye')



