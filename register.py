from tkinter import *
#from tkinter import messagebox


def register_window():

    from tkinter import messagebox


    root = Toplevel()
    root.title("Register")
    root.geometry("500x300")
    frame = Frame(root,pady=20, )

    email_str = StringVar()
    login = Entry(frame, textvariable=email_str, font=("Arial", 18))
    login_lable = Label(frame, text = "Email: ", font=("Arial", 18))
    login_lable.grid(column = 0, row = 0)
    login.grid( column = 1, row = 0)



    email_str_repeat = StringVar()
    login_repeat = Entry(frame, textvariable=email_str_repeat, font=("Arial", 18))
    login_lable_repeat = Label(frame, text = "Ter controle nog maals Email: ", font=("Arial", 12))
    login_lable_repeat.grid(column = 0, row=1)
    login_repeat.grid(column = 1, row =1)

    password_str = StringVar()
    password_lable = Label(frame, text = "Password: ", font=("Arial", 18))
    password = Entry(frame, text = "Password: ", textvariable=password_str,font=("Arial", 18))
    password.grid(column = 1, row = 2)
    password_lable.grid(column = 0, row = 2)

    buttons_frame = Frame(root, )
    def cancel ():
        root.destroy()

    cancel_button = Button(buttons_frame,text = "Annuleren", font=("Arial", 13), relief = GROOVE, command=cancel)
    cancel_button.grid(column = 1,row = 2, pady = 10,padx = 30)




    def register():


        if "@" in email_str.get() and password_str.get() != "" and email_str_repeat.get()==email_str.get():
            messagebox.showinfo(title="Registered!", message="You have sucessfully registered!")
            root.destroy()
        else:
            messagebox.showerror(title="Error", message="You have not filled the forms correctly")


    register_button = Button(buttons_frame, text = "Register", font=("Arial", 13), relief = GROOVE, command = register)
    register_button.grid(column= 0, row = 2, )

    frame.pack()
    buttons_frame.pack()
    root.mainloop()
    '''
        def login_func():
            if "@" in email_str.get() and password_str.get()!="":
                messagebox.showinfo(title="success!", message = "You have successfully loged in!")
                root.destroy()
            else:
                messagebox.showerror(title="Error", message = "You've not filled the forms correctly")
        login_button = Button(buttons_frame, text = "Login",font=("Arial", 13),relief = GROOVE, command=login_func )
        login_button.grid(column = 2, row =2)
        frame.pack()
        buttons_frame.pack()
    '''