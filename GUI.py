'''
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)
        self.label = Label(master, text="Total:")
        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.multiplication_button = Button(master, text="x", command=lambda: self.update("multiplication"))
        self.divide_button = Button(master, text="/", command=lambda: self.update("divide"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.multiplication_button.grid(row=3, column=0)
        self.divide_button.grid(row=3, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False
    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "multiplication":
            self.total *= self.entered_number
        elif method == "divide":
            if self.entered_number != 0:
                self.total /= self.entered_number
            else:
                self.total_label_text.set("Error: Division by zero")
        else: # reset
            self.total = 0
            self.total_label_text.set(self.total)
            self.entry.delete(0, END)
 
root = Tk()
my_gui = Calculator(root)
root.mainloop()
'''
import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        pass

def mark_as_completed():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(selected_task_index, {'bg': 'light gray', 'fg': 'gray'})
    except IndexError:
        pass

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Set background color for the window
root.configure(bg="white")

# Create and place widgets
label_title = tk.Label(root, text="To-Do List", font=("Helvetica", 16), bg="white")
label_title.pack(pady=10)

entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)

button_add = tk.Button(root, text="Add Task", width=15, command=add_task, bg="light blue", fg="white")
button_add.pack(pady=5)

button_remove = tk.Button(root, text="Remove", width=15, command=remove_task, bg="red", fg="white")
button_remove.pack(pady=5)

button_completed = tk.Button(root, text="Mark as Completed", width=15, command=mark_as_completed, bg="green", fg="white")
button_completed.pack(pady=5)

listbox_tasks = tk.Listbox(root, height=15, width=50, font=("Helvetica", 12), bg="light yellow")
listbox_tasks.pack(padx=10, pady=10)

# Run the main event loop
root.mainloop()
