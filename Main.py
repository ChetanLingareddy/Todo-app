

while True:
    user_action= input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input ("Enter a To-do : ") + "\n"

            file = open('Todo.txt','r')
            todos=file.readlines()
            file.close()

            todos.append(todo)

            file = open('Todo.txt','w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('Todo.txt','r')
            todos = file.readlines()
            file.close()

            for index,x in enumerate(todos):
                x= x.capitalize()
                x=x.strip('\n')
                row = f"{index + 1}-{x}"
                print(row)
        case 'edit':
            number  = int(input("enter a To-do list number to edit: "))
            new_number = number -1
            new_todo= input("enter your new To-do: ")
            todos[new_number]=new_todo
        case 'complete':
            number = int(input("Enter a To-do list number to complete: "))
            todos.pop(number - 1)
        case 'exit':

            break
print ('bye')



