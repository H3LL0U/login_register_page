import sqlite3
from tkinter import *
from tkinter import ttk
def lege_app():
    from tkinter import messagebox
    geo = "250x100"
    root = Tk()
    root.geometry(geo)
    frame = Frame(root)
    frame.pack()


    label = Label(frame, text="Voer je naam in:")

    label.grid(column=1, row = 0)


    selected_account_name = StringVar()
    def get_naam_database():
        global accounts
        global labels_namen
        global labels_adressen
        global labels_woonplaatsen
        try:
            conn = sqlite3.connect('Register.db')
            cur = conn.cursor()
            get_name = f"SELECT naam, adress, woonplaats FROM register WHERE naam = '{selected_account_name.get()}';"
            cur.execute(get_name)
            data = cur.fetchall()
            accounts = data
            conn.close()
            labels_namen = []
            labels_adressen = []
            labels_woonplaatsen = []
            for i in accounts:
                
                labels_namen.append(list(i)[0])
                labels_adressen.append(list(i)[1])
                labels_woonplaatsen.append(list(i)[2])
            
            for idx, i in enumerate(labels_namen):
                Label(frame,text = i).grid(column=0, row = idx+4)
            for idx, i in enumerate(labels_adressen):
                Label(frame, text = i).grid(column=1, row = idx+4 )
            for idx, i in enumerate(labels_woonplaatsen):
                Label(frame, text = i).grid(column=2, row = idx+4)
            
                
        except sqlite3.Error as error:
            conn.close()
            print("something wen wrong",  error)
            
    
    accounts = []
    
    combobox = ttk.Combobox(frame,values = accounts, textvariable= selected_account_name)
    combobox.grid( column=1, row =1)
    submit_button = Button(frame,text = "Select", command=get_naam_database)
    submit_button.grid(row=2, column=1)







    root.geometry(geo)








    root.mainloop()