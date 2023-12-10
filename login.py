import sqlite3
from tkinter import *
from tkinter import messagebox
from register import register_window
from lege_pagina import lege_app
root = Tk()
root.title("login")
root.geometry("500x300")
frame = Frame(root,pady=20, )

email_str = StringVar()
login = Entry(frame, textvariable=email_str, font=("Arial", 18))
login_lable = Label(frame, text = "Email: ", font=("Arial", 18))
login_lable.grid(column = 0, row = 0)
login.grid( column = 1, row = 0)

password_str = StringVar()
password_lable = Label(frame, text = "Password: ", font=("Arial", 18))
password = Entry(frame, text = "Password: ", textvariable=password_str,font=("Arial", 18))
password.grid(column = 1, row = 1)
password_lable.grid(column = 0, row = 1)



buttons_frame = Frame(root, )
def cancel ():
    root.destroy()

cancel_button = Button(buttons_frame,text = "Annuleren", font=("Arial", 13), relief = GROOVE, command=cancel)
cancel_button.grid(column = 1,row = 2, pady = 10,padx = 30)




def register():
    register_window()

register_button = Button(buttons_frame, text = "Register", font=("Arial", 13), relief = GROOVE, command = register)
register_button.grid(column= 0, row = 2, )
def check_for_existing_accounts():
    try:
        conn = sqlite3.connect("Register.db")
        cur = conn.cursor()
        get_passwords_and_emails = "SELECT wachtwoord, email FROM register"
        cur.execute(get_passwords_and_emails)
        data = cur.fetchall()
        conn.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if conn:
            conn.close()
        return data


def login_func():
    data = check_for_existing_accounts()
    for i in data:
        if [password_str.get(), email_str.get()] == list(i):
        #if "@" in email_str.get() and password_str.get()!="":
            messagebox.showinfo(title="success!", message = "You have successfully loged in!")

            root.destroy()
            lege_app()

    else:
        messagebox.showerror(title="Error", message = "You've not filled the forms correctly")
login_button = Button(buttons_frame, text = "Login",font=("Arial", 13),relief = GROOVE, command=login_func )
login_button.grid(column = 2, row =2)
frame.pack()
buttons_frame.pack()


root.mainloop()


