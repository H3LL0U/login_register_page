import sqlite3
from tkinter import *
from tkinter import ttk
def lege_app():
    from tkinter import messagebox
    geo = "500x300"
    root = Tk()
    root.geometry(geo)
    frame = Frame(root)
    frame.pack()


    label = Label(frame, text="Voer je naam in:")

    label.grid(column=1, row = 0)


    selected_account_name = StringVar()
    def get_all_names():
        try:
            conn = sqlite3.connect("Register.db")
            cur = conn.cursor()
            select_names = "Select naam FROM register"
            cur.execute(select_names)
            data = cur.fetchall()
            conn.close()
            return data
        except sqlite3.Error as error:
            print(error)
        finally:
            if conn:
                conn.close()
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
            print("something went wrong",  error)
            
    
    accounts = get_all_names()
    
    combobox = ttk.Combobox(frame,values = accounts, textvariable= selected_account_name)
    combobox.grid( column=1, row =1)
    submit_button = Button(frame,text = "Select", command=get_naam_database)
    submit_button.grid(row=2, column=1)


    frame_artsen = Frame(root)
    frame_artsen.pack()
    ziektes_select_list = StringVar(value=["Leukemie", "Kanker", "Taalstoornis", "Diabetes", "Astma"])
    ziektes_select_label = Label(frame_artsen,text = "Ziekte: ")
    ziektes_select_label.grid(column = 0, row = 0)
    ziektes_select = Listbox(frame_artsen, listvariable=ziektes_select_list , selectmode="single", exportselection = False)
    ziektes_select.grid(column = 1, row = 0)

    artsen_select_list = StringVar(value=["Dr. Jansen", "Dr. de Vries", "Dr. Bakker", "Dr. van der Meer"])
    arts_select_label = Label(frame_artsen,text = "Arts: ")
    arts_select_label.grid(column = 2, row = 0)
    arts_select = Listbox(frame_artsen, listvariable=artsen_select_list, selectmode="single", exportselection = False)
    arts_select.grid(column = 3, row = 0 )
    def update_Label(event):

        selected_items = arts_select.curselection()
        selectedid_arts = "".join(arts_select.get(i) for i in selected_items)
        selectedid_ziekte = "".join(ziektes_select.get(i) for i in ziektes_select.curselection())
        a = Label(root, text=f"U heeft gekozen voor {selectedid_arts} voor een behandeling voor {selectedid_ziekte}.")
        #for widget in root.winfo_children():
            #if isinstance(widget, Label) and widget.winfo_exists():
                #widget.destroy()
        if selectedid_ziekte and selectedid_arts:


            a.pack()


    arts_select.bind("<<ListboxSelect>>", update_Label)
    ziektes_select.bind("<<ListboxSelect>>", update_Label)














    root.mainloop()