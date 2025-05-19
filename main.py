import tkinter as tk
from tkinter import messagebox
from atm_logic import user_account

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='👁️')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='🙈')

def login():
    username_input = username_entry.get()
    password_input = password_entry.get()

    if username_input == 'fardwish' and password_input == '212':
        messagebox.showinfo("Login Success", "Access granted.")
        root.destroy()
        user_account()
    else:
        messagebox.showerror("Error", "Invalid credentials")

root = tk.Tk()
root.title("ATM Login")
root.geometry("300x200")

tk.Label(root, text="Username:").pack()
username_entry = tk.Entry(root)
username_entry.pack()

tk.Label(root, text="Password:").pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

toggle_btn = tk.Button(root, text='👁️', command=toggle_password)
toggle_btn.pack()

login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack(pady=10)

root.mainloop()
