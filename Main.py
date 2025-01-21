

while True:
    user_action= input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input ("Enter a To-do : ") + "\n"
            # this code lines are for writing text in to the text files in traditional way
            """""
            file = open('Todo.txt','r')
            todos=file.readlines()
            file.close()
            """
            # Below code is the modified version of the above traditional code which is error free

            with open("Todo.txt",'r')  as file:
                todos = file.readlines()

            todos.append(todo)
            #this code lines are for writing text in to the text files in traditional way
            """
            file = open('Todo.txt','w')
            file.writelines(todos)
            file.close()
            """
            # Below code is the modified version of the above traditional code which is error free
            with open('Todo.txt','w') as file:
                file.writelines(todos)

        case 'show':
            """
            file = open('Todo.txt','r')
            todos = file.readlines()
            file.close()
            """
            with open("Todo.txt",'r')  as file:
                todos = file.readlines()

            for index,x in enumerate(todos):
                x= x.capitalize()
                x=x.strip('\n')
                row = f"{index + 1}-{x}"
                print(row)
        case 'edit':
            number  = int(input("enter a To-do list number to edit: "))
            new_number = number -1

            with open("Todo.txt",'r') as file:
                todos = file.readlines()

            new_todo= input("enter your new To-do: ")
            todos[new_number]=new_todo + "\n"

            with open("Todo.txt",'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Enter a To-do list number to complete: "))

            with open("Todo.txt",'r') as file:
                todos = file.readlines()

            index = number -1
            Item_to_remove = todos[index].strip()

            todos.pop(index)

            with open("Todo.txt",'w') as file:
                file.writelines(todos)

            message = f"Todo {Item_to_remove} is removed from the string"
            print(message)

        case 'exit':
            break
print ('bye')



