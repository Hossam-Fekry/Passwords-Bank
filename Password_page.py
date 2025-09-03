from customtkinter import *
import json
import subprocess
from tkinter import messagebox 
from cryptography.fernet import Fernet

with open("settings.json", "r") as settings_file:
    settings = json.load(settings_file)

root = CTk()
root.title("Password Page")
root.geometry("495x298")
root.resizable(0, 0)
set_appearance_mode(settings["Theme"])
root.iconbitmap("icon.ico")

#make the functions

def exit(event = None):
    root.destroy()

def submit(event = None):
    user_pssword = password_entry.get()
    with open("p_key.key", "rb") as key_file:
        key = key_file.read()
        cipher = Fernet(key)
        decrypted_password = cipher.decrypt(settings["MasterPassword"].encode()).decode()
    if user_pssword == "":
        messagebox.showerror("Error", "Please enter a password")
        password_entry.focus()
        return
    if user_pssword == decrypted_password:
        root.destroy()
        subprocess.run(["python", "Home Page.py"])
    else:
        password_entry.delete(0, 'end')
        messagebox.showerror("Error", "Incorrect Password")
#make the title

CTkLabel(root, text="Enter your password", font=("Arial", 24,"bold")).pack(pady=30)

#make the password entry

password_entry = CTkEntry(root, font=("Arial", 20), corner_radius=25, width=300, placeholder_text="Enter the Password")
password_entry.pack(pady = 30)

#make the buttons

SubmitButton = CTkButton(root, text="Submit",fg_color = "#2C73D2" ,hover_color = "#1E56A0",corner_radius = 25,font=("Arial", 20,"bold") ,command=submit)
SubmitButton.place(x = 90 ,y = 200)

ExitButton = CTkButton(root, text="Exit",fg_color = "#B00020" ,hover_color = "#8C001A",corner_radius = 25,font=("Arial", 20,"bold") ,command=exit)
ExitButton.place(x = 260 ,y = 200)

root.bind("<Return>", submit)
root.bind("<Escape>", exit)
root.mainloop()
