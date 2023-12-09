from tkinter import *
import sqlite3
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

    naam_str = StringVar()
    naam_lable = Label(frame, text="Naam: ", font=("Arial", 18))
    naam = Entry(frame, text="Naam: ", textvariable=naam_str, font=("Arial", 18))
    naam.grid(column=1, row=3)
    naam_lable.grid(column=0, row=3)

    adress_str = StringVar()
    adress_lable = Label(frame, text="Adres: ", font=("Arial", 18))
    adress = Entry(frame, text="Adres: ", textvariable=adress_str, font=("Arial", 18))
    adress.grid(column=1, row=4)
    adress_lable.grid(column=0, row=4)

    woonplaats_str = StringVar()
    woonplaats_lable = Label(frame, text="Woonplaats: ", font=("Arial", 18))
    woonplaats = Entry(frame, text="Woonplaats: ", textvariable=woonplaats_str, font=("Arial", 18))
    woonplaats_lable.grid(column=0, row=5)
    woonplaats.grid(column=1, row=5)

    buttons_frame = Frame(root, )
    def cancel ():
        root.destroy()

    cancel_button = Button(buttons_frame,text = "Annuleren", font=("Arial", 13), relief = GROOVE, command=cancel)
    cancel_button.grid(column = 1,row = 2, pady = 10,padx = 30)

    def send_data_to_database():
        try:
            conn = sqlite3.connect('Register.db')
            cursor = conn.cursor()
            create_table = f"CREATE TABLE IF NOT EXISTS register (id INTEGER PRIMARY KEY, adress TEXT, woonplaats TEXT, naam TEXT, wachtwoord TEXT, email TEXT);"
            cursor.execute(create_table)
            send_data = f"INSERT INTO register (adress, woonplaats, naam, wachtwoord, email) VALUES( '{adress_str.get()}','{woonplaats_str.get()}','{naam_str.get()}','{password_str.get()}', '{email_str.get()}');"
            cursor.execute(send_data)
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            print("something went wrong", error)
            conn.close()
    def register():


        if "@" in email_str.get() and password_str.get() != "" and email_str_repeat.get()==email_str.get() and woonplaats_str.get()!="" and naam_str.get()!="" and adress_str!="":
            messagebox.showinfo(title="Registered!", message="You have sucessfully registered!")
            send_data_to_database()
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