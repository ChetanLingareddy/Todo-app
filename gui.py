import FreeSimpleGUI as Sg
import functions

label = Sg.Text( "Enter a To-do" )
input_box = Sg.InputText( tooltip ="Enter a To-do", key="todo" )
add_button = Sg.Button( "Add" )
exit_button = Sg.Button("Exit")

window = Sg.Window( 'My To-do App',
                    layout=[[label],[input_box,add_button],[exit_button]],
                    font=('Helvetica',15) )

while True:
    events, values =window.read()
    match events:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Exit":
            break
window.close()
