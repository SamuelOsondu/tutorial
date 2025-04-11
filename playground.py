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
