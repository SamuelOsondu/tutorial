# ✅ 1. Basic Calculator

import tkinter as tk

# Initialize main window
root = tk.Tk()
root.geometry('300x400')
root.title('Simple Calculator')

expression = ""

# Function to update expression in the display
def press(key):
    global expression
    expression += str(key)
    display_var.set(expression)

# Function to evaluate the final expression
def equal_press():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result  # You can continue calculating with the result
    except:
        display_var.set("Error")
        expression = ""

# Function to clear the display
def clear():
    global expression
    expression = ""
    display_var.set("")

# StringVar to update label text
display_var = tk.StringVar()

# Display label
display = tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="white", anchor="w", relief="sunken", height=2)
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        action = equal_press
    elif text == 'C':
        action = clear
    else:
        action = lambda x=text: press(x)

    tk.Button(root, text=text, width=5, height=2, font=("Arial", 16), command=action).grid(row=row, column=col, padx=5, pady=5)

# Make all rows and columns expand equally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()


# ✅ Simple To-Do List App

import tkinter as tk
from tkinter import messagebox

# --- Setup window ---
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x450")

tasks = []

# --- Functions ---
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# --- Widgets ---
tk.Label(root, text="To-Do List", font=("Arial", 24)).pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, height=10, width=45, font=("Arial", 12))
task_listbox.pack(pady=20)

# --- Start the app ---
root.mainloop()






# ✅ 3. Login Form (with show/hide password)

import tkinter as tk
from tkinter import messagebox

def login():
    user = username_entry.get()
    pwd = password_entry.get()
    if user == "admin" and pwd == "1234":
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login", "Invalid credentials!")

def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_btn.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_btn.config(text="Hide")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x200")

tk.Label(root, text="Username").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

toggle_btn = tk.Button(root, text="Show", command=toggle_password)
toggle_btn.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()


# ✅ 4. Paint App (Canvas Drawing)

import tkinter as tk

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x-2, y-2, x+2, y+2, fill=color)

def set_color(new_color):
    global color
    color = new_color

def clear_canvas():
    canvas.delete("all")

root = tk.Tk()
root.title("Paint App")
color = "black"

canvas = tk.Canvas(root, bg="white", width=500, height=400)
canvas.pack()

canvas.bind("<B1-Motion>", draw)

colors = ["black", "red", "blue", "green", "purple"]
for c in colors:
    tk.Button(root, bg=c, width=3, command=lambda c=c: set_color(c)).pack(side="left")

tk.Button(root, text="Clear", command=clear_canvas).pack(side="right")

root.mainloop()


# ✅ 5. Form with Validation

import tkinter as tk
from tkinter import messagebox
import re

def submit_form():
    name = name_entry.get()
    email = email_entry.get()

    if not name:
        messagebox.showerror("Error", "Name is required!")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format!")
    else:
        messagebox.showinfo("Success", "Form submitted!")

root = tk.Tk()
root.title("Form with Validation")
root.geometry("300x200")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=10)

root.mainloop()



# ✅ 6. File Explorer


import tkinter as tk
from tkinter import filedialog, messagebox

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, "r") as f:
                content = f.read()
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_area.get(1.0, tk.END))

root = tk.Tk()
root.title("Simple File Explorer")

text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

tk.Button(root, text="Open", command=open_file).pack(side="left")
tk.Button(root, text="Save", command=save_file).pack(side="right")

root.mainloop()



# ✅ 7. Simple Chat GUI (Simulated)

import tkinter as tk

def send_message():
    msg = entry.get()
    if msg.strip():
        chat.insert(tk.END, f"You: {msg}")
        entry.delete(0, tk.END)
        chat.insert(tk.END, f"Bot: {reply(msg)}\n")

def reply(msg):
    return "Nice!" if "hello" in msg.lower() else "I don't understand."

root = tk.Tk()
root.title("Chat App")

chat = tk.Listbox(root, width=50, height=15)
chat.pack()

entry = tk.Entry(root, width=40)
entry.pack(side="left", padx=5, pady=5)

tk.Button(root, text="Send", command=send_message).pack(side="right", padx=5)

root.mainloop()



# ✅ 8. Tic-Tac-Toe Game

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
buttons = [[None]*3 for _ in range(3)]

def check_winner():
    for i in range(3):
        if all(buttons[i][j]["text"] == current_player for j in range(3)) or \
           all(buttons[j][i]["text"] == current_player for j in range(3)):
            return True
    if all(buttons[i][i]["text"] == current_player for i in range(3)) or \
       all(buttons[i][2-i]["text"] == current_player for i in range(3)):
        return True
    return False

def click(r, c):
    global current_player
    if buttons[r][c]["text"] == "":
        buttons[r][c]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Winner!", f"{current_player} wins!")
            reset()
        elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Draw", "It's a draw!")
            reset()
        else:
            current_player = "O" if current_player == "X" else "X"

def reset():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3,
                                  command=lambda r=i, c=j: click(r, c))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()


