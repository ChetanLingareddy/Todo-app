import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter a To-do")
input_box = sg.InputText(tooltip = "Enter a To-do")
add_button = sg.Button("Add")

window = sg.Window('My To-do App', layout=[[label],[input_box,add_button]])
window.read()
window.close()
