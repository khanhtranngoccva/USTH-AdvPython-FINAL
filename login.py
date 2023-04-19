from tkinter import* #importing all the classes and methods
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk #importing jpg images
from manager import get_user


def login_ui():
    window = tk.Tk()

    success = False

    def login():
        nonlocal success, user_name_input_area, user_password_entry_area

        user_name = user_name_input_area.get()
        user_password = user_password_entry_area.get()

        if not user_name or not user_password:
            messagebox.showerror("Error", "Please enter username and password.")
            return
        result = get_user(user_name=user_name, password=user_password)
        if not result:
            messagebox.showerror("Error", "Username or password is incorrect.")
        else:
            window.quit()
            window.destroy()
            success = True

    window.title("Login")
    window.geometry("400x500")
    window.resizable(False,False)
    window.configure(bg='#FFEBCD')

    logo =Label(window,bd=50,text="LOGIN",fg="red",bg='#FFEBCD',font=("yu gothic ui",30,"bold"))
    logo.pack(side=TOP,fill=X)

    Label(window,text = "Username",font=("yu gothic ui",13,"bold"),bg='#FFEBCD').place(x = 40,y = 180) 
    user_name_input_area = Entry(window, font=("yu gothic ui",13,"bold"), width = 30)
    user_name_input_area.place(x = 130, y = 180,width=200,height=30)

    Label(window,text = "Password",font=("yu gothic ui",13,"bold"),bg='#FFEBCD').place(x = 40,y = 230) 
    user_password_entry_area = Entry(window, show='*', font=("yu gothic ui",13,"bold"), width = 30)
    user_password_entry_area.place(x = 130, y = 230,width=200,height=30)

    def show_password():
        if user_password_entry_area.cget('show') == '*':
            user_password_entry_area.config(show='')
        else:
            user_password_entry_area.config(show='*')

    check_button = Checkbutton(window, text="Show password", command=show_password, font=("yu gothic ui",8,"bold"),bg='#FFEBCD')
    check_button.place(x=40, y=280)

    Button(window,text = "Login",font=("bold"), command=login).place(x = 150,y = 330,width=100) 
    window.mainloop()
    
    return success