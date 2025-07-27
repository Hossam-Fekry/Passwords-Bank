from customtkinter import *
import subprocess
import json
import string
import random
from tkinter import messagebox
import os

root = CTk()
root.title("New Account")
root.geometry("471x457")

DATA_FILE = "passwords.json"

def go_main():
    root.destroy()
    subprocess.run(["python", "Home Page.py"])

def Show_Password():
    root.destroy()
    subprocess.run(["python", "Show Passwords.py"])



def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}  # لو الملف فاضي أو فيه مشكلة في التنسيق
    else:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()_+"
    all_chars = letters + numbers + symbols
    password = ''.join(random.choice(all_chars) for _ in range(12))
    Password_Entry.delete(0, END)
    Password_Entry.insert(0, password)

def save_password():
    website = Website_Entry.get().strip()
    username = username_Entry.get().strip()
    password = Password_Entry.get().strip()

    if not website or not username or not password:
        messagebox.showwarning("Empty Fields", "Please Fill all the Fields  ⚠")
        return

    data = load_data()
    data[website] = {"username": username, "password": password}
    save_data(data)
    messagebox.showinfo("Done", "Saving password done ✔" )

    Website_Entry.delete(0, END)
    username_Entry.delete(0, END)
    Password_Entry.delete(0, END)

CTkLabel(root, text="New Account", font=("Arial", 24,"bold")).pack(pady=30)

CTkLabel(root, text="The Website", font=("Arial", 16,"bold")).place(x = 20, y = 130)
Website_Entry = CTkEntry(root, font=("Arial", 20), corner_radius=25, width=200, placeholder_text="Enter the Website")
Website_Entry.place(x = 150, y = 130)

CTkLabel(root, text="user name or Email", font=("Arial", 16,"bold")).place(x = 20, y = 180)
username_Entry = CTkEntry(root, font=("Arial", 20), corner_radius=25, width=210, placeholder_text="Enter the username")
username_Entry.place(x = 170, y = 180)


CTkLabel(root, text="The Password", font=("Arial", 16,"bold")).place(x = 20, y = 230)
Password_Entry = CTkEntry(root, font=("Arial", 20), corner_radius=25, width=310, placeholder_text="Enter the Password if you have")
Password_Entry.place(x = 150, y = 230)

Save_password_Button = CTkButton(root, text="Save Password",fg_color = "#2C73D2" ,hover_color = "#1E56A0",corner_radius = 25,font=("Arial", 20,"bold") ,command=save_password)
Save_password_Button.place(x = 20 ,y = 300)

Generate_Password_Button = CTkButton(root, text="Generate Password",fg_color = "#2C73D2" ,hover_color = "#1E56A0",corner_radius = 25,font=("Arial", 20,"bold"), command=generate_password)
Generate_Password_Button.place(x = 250 ,y = 300)

back_button = CTkButton(root, text="Back to main", fg_color="#333333", hover_color="#0F0F0F", corner_radius=5, font=("Arial", 20, "bold"), command=go_main)
back_button.place(x=20, y=400)

root.mainloop()