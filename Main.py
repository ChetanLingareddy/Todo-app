def get_todos(filepath = "Todo.txt"):
    """Reads a text file and returns a list of to- do items."""
    with open ( filepath, 'r' ) as file_local :
        todos_local = file_local.readlines ()
    return todos_local

def write_todos(todos_arg,filepath = "Todo.txt" ):
    """ Writes the to-do items list to the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action= input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):

        #todo = input ("Enter a To-do : ") + "\n"
        """This code lines are for writing text in to the text files in traditional way"""
        """
        file = open('Todo.txt','r')
        todos=file.readlines()
        file.close()
        """
        # Below code is the modified version of the above traditional code which is error free
        todo = "\n" + user_action[4:]

        todos = get_todos()

        todos.append(todo)
        #this code lines are for writing text in to the text files in traditional way
        """
        file = open('Todo.txt','w')
        file.writelines(todos)
        file.close()
        """
        # Below code is the modified version of the above traditional code which is error free
        write_todos(todos)

    elif user_action.startswith("show"):
        """
        file = open('Todo.txt','r')
        todos = file.readlines()
        file.close() 
        """
        todos = get_todos ()

        for index,x in enumerate(todos):
            x= x.capitalize()
            x=x.strip('\n')
            row = f"{index + 1}-{x}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number  = int(user_action[5:])
            new_number = number -1

            todos = get_todos()

            new_todo= input("enter your new To-do: ")
            todos[new_number]=new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Enter a valid number to edit.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number -1
            Item_to_remove = todos[index].strip()

            todos.pop(index)

            write_todos(todos)

            message = f"Todo {Item_to_remove} is completed."
            print(message)
        except IndexError:
            print("enter a valid number.")

    elif user_action.startswith("exit"):
        break
    else:
        print("Enter a valid command.")
print ('bye')



