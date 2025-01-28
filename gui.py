import FreeSimpleGUI as Sg
import functions

label = Sg.Text( "Enter a To-do" )
input_box = Sg.InputText( tooltip ="Enter a To-do", key="todo" )
add_button = Sg.Button( "Add" )
list_box = Sg.Listbox(values=functions.get_todos(),key='todos',
                      enable_events=True, size = [44 , 10])
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window( 'My To-do App',
                    layout=[[label],[input_box,add_button],[list_box,edit_button],[exit_button]],
                    font=('Helvetica',15) )

while True:
    events, values =window.read()
    print(events)
    print(values)
    match events:

        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values= todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)
        case "todos":
            window['todo'].update(value= values['todos'][0])
        case "Exit":
            break
window.close()
