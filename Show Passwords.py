#TODO: Import necessary modules
import os
from customtkinter import *
from tkinter import messagebox
import subprocess
import tkinter as tk
import json
import pyperclip

DATA_FILE = "passwords.json"

def copy_selected_password():
    selected_index = passwords_listbox.curselection()
    if selected_index:
        selected = passwords_listbox.get(selected_index)
        site = selected.split(" | ")[0]
        data = load_data()
        if site in data:
            pyperclip.copy(data[site]["password"])
            messagebox.showinfo("copy done","the password for {site} is copied to the clipboard")


def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                content = f.read().strip()
                if not content:
                    return {}  
                return json.loads(content)
        except json.JSONDecodeError:
            return {}  
    else:
        return {}



def go_main():
    root.destroy()
    subprocess.run(["python", "Home Page.py"])

root = CTk()
root.geometry("604x455")


CTkLabel(root, text="Saved Accounts", font=("Arial", 24)).pack(pady=20) 

passwords_listbox = tk.Listbox(root, width=75, height=15)
passwords_listbox.pack(pady=10)

copy_btn = CTkButton(root, text="Copy Selected Password", command=copy_selected_password, corner_radius=25, font=("Arial", 16, "bold"))
copy_btn.pack(pady=15)

back_button = CTkButton(root, text="Back to main", fg_color="#333333", hover_color="#0F0F0F", corner_radius=5, font=("Arial", 20, "bold"), command=go_main)
back_button.place(x=20, y=400)

def update_passwords_list():
    passwords_listbox.delete(0, tk.END)
    data = load_data()
    for site, creds in data.items():
        passwords_listbox.insert(tk.END, f"{site} | {creds['username']}")



#load the data from the file
update_passwords_list()

root.mainloop()