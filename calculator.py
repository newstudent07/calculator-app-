#importing 
import tkinter as tk 
from tkinter import messagebox  
#functions 
def on_click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button)

def clear():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

def all_clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

#creating the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#050607")

#display entry
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

#buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '.', '+',
    'AC', '=' 
]
btn_params = {'font': ("Arial", 18), 'width': 5, 'height': 2, 'borderwidth': 1, 'relief': "raised"}
row_values = 1
col_values = 0

for button in buttons:
    if button == 'C':
        action = clear
    elif button == 'AC':
        action = all_clear
    elif button == '=':
        action = calculate
    else:
        action = lambda x=button: on_click(x)
    tk.Button(root, text=button, command=action, **btn_params).grid(row=row_values, column=col_values, padx=5, pady=5)
    col_values += 1
    if col_values >3:
        col_values = 0
        row_values += 1


root.mainloop()

