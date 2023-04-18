from tkinter import* #importing all the classes and methods
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk #importing jpg images
import pymysql
from manager import get_user


def login_ui():
    root = Tk()

    success = False

    def login():
        nonlocal success, user_name_input_area, user_password_entry_area

        user_name = user_name_input_area.get()
        user_password = user_password_entry_area.get();

        if not user_name or not user_password:
            messagebox.showerror("Error", "Please enter username and password.")
            return
        result = get_user(user_name=user_name, password=user_password)
        if not result:
            messagebox.showerror("Error", "Username or password is incorrect.")
        else:
            root.destroy()
            success = True

    root.title("Login")
    root.geometry("400x500")
    root.configure(bg='#FFEBCD')
    logo =Label(root,bd=50,text="LOGIN",fg="red",bg='#FFEBCD',font=("times new roman",30,"bold"))
    logo.pack(side=TOP,fill=X)

    Label(root,text = "Username",font=("times new roman",13,"bold"),bg='#FFEBCD').place(x = 40,y = 180) 
    user_name_input_area = Entry(root, font=("times new roman",13,"bold"), width = 30)
    user_name_input_area.place(x = 130, y = 180,width=200,height=30)
    Label(root,text = "Password",font=("times new roman",13,"bold"),bg='#FFEBCD').place(x = 40,y = 230) 
    user_password_entry_area = Entry(root, font=("times new roman",13,"bold"), width = 30)
    user_password_entry_area.place(x = 130, y = 230,width=200,height=30)
    Button(root,text = "Login",font=("bold"), command=login).place(x = 150,y = 300,width=80) 

    root.mainloop()
    return success