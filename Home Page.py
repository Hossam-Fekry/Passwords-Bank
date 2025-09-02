#importing the moudules
from customtkinter import *
import subprocess
from tkinter import messagebox

root = CTk()
root.title("Home Page")
root.geometry("510x298")
root.resizable(0,0)
root.iconbitmap("icon.ico")
#make the functions

def close_app(event = None):
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
        root.destroy()

def New_Account():
    root.destroy()
    subprocess.run(["python", "New Account.py"])

def Show_Passwords():
    root.destroy()
    subprocess.run(["python", "Show Passwords.py"])

# make the app title

CTkLabel(root, text="Select Your Action", font=("Arial", 24,"bold")).pack(pady=30)

# make the buttons

New_Account_Button = CTkButton(root, text="New Account",fg_color = "#2C73D2" ,hover_color = "#1E56A0",corner_radius = 25,font=("Arial", 20,"bold") ,command=New_Account)
New_Account_Button.place(x = 50 ,y = 150)

Show_Passwords_Button = CTkButton(root, text="Show Accounts",fg_color = "#2C73D2" ,hover_color = "#1E56A0",corner_radius = 25,font=("Arial", 20,"bold") ,command=Show_Passwords)
Show_Passwords_Button.place(x = 300 ,y = 150)

ExitButton = CTkButton(root, text="Exit",fg_color = "#B00020" ,hover_color = "#8C001A",corner_radius = 25,font=("Arial", 20,"bold") ,command=close_app)
ExitButton.pack(pady=40, side = BOTTOM)

root.bind('<Escape>', close_app)


root.mainloop()