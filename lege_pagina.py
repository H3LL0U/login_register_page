import sqlite3
from tkinter import *
from tkinter import ttk
#create a new window after being logged in
def lege_app():
    from tkinter import messagebox
    geo = "500x300"
    root = Tk()
    root.geometry(geo)
    frame = Frame(root)
    frame.pack()
    #initializing accounts variable for the Listbox with names of the doctors
    accounts = StringVar(value=[])
    #initial lable

    Label(frame,text="Koppel een specialist aan een ziektebeeld").pack()

    #Radiobuttons

    radio_buttons_frame = Frame(root)
    radio_buttons_frame.pack()
    #set values
    gekozen_artsen = []
    def set_value(variable, new_value):
        nonlocal gekozen_artsen
        nonlocal Listboxes
        Listboxes[0].delete(0,'end')

        
        
        for i in new_value:
            Listboxes[0].insert('end', i)
        
        gekozen_artsen = list(new_value)
        gekozen_artsen = [" ".join(i) for i in gekozen_artsen]
        
            
        
        
    
    def get_doctor_names_from_database():
        nonlocal accounts
        nonlocal Listboxes
        data = ()
        try:
            conn = sqlite3.connect('Artsen.db')
            cur = conn.cursor()
            get_name = f"SELECT name, last_name FROM register"
            cur.execute(get_name)
            data = cur.fetchall()
            set_value(accounts,data)
            
            conn.close()
        except sqlite3.Error as error:
            print(error)
        finally:
            conn.close()
    def remove_doctors():
        gekozen_artsen = []
        Listboxes[0].delete(0, "end")
    Radiobuttons_value = IntVar()
    Radiobuttons_value.set(1)
    radio_buttons = [Radiobutton(radio_buttons_frame,text="Database",variable= Radiobuttons_value, value=1, command=get_doctor_names_from_database),
                     Radiobutton(radio_buttons_frame,text="Bestand",variable=Radiobuttons_value,value=2, command=remove_doctors),
                     Radiobutton(radio_buttons_frame,text="Tekstveld",variable=Radiobuttons_value , value=3, command= remove_doctors)
                     ]
    for idx, i in enumerate(radio_buttons):
        i.grid(column=idx,row=0)

    #Entry field with radio_buttons functions
        
    frame_for_selection = Frame(root)
    frame_for_selection.pack()
    
    entry_selection_variable = StringVar()
    entry_selection_variable.set("2")
    Radiobuttons_value_selection_frame = IntVar()
    Radiobuttons_value_selection_frame.set(1)
    objects_of_the_selection_frame = [Entry(frame_for_selection,textvariable = entry_selection_variable ), 
                                    Radiobutton(frame_for_selection,text = "Specialist",variable=Radiobuttons_value_selection_frame,value=1),
                                    Radiobutton(frame_for_selection,text="Ziektebeeld",variable=Radiobuttons_value_selection_frame,value=2)
                                    ]
    for idx,i in enumerate(objects_of_the_selection_frame):
        i.grid(column=idx,row=0)
    #Listboxes
    Listbox_frame = Frame(root)
    Listbox_frame.pack()
    ziektes = ["Leukemie", "Kanker", "Taalstoornis", "Diabetes", "Astma"]
    Listboxes = [Listbox(Listbox_frame, height=10,listvariable=accounts, exportselection=False),Listbox(Listbox_frame,height=10,listvariable=ziektes, exportselection=False)]
    for idx, a in enumerate(Listboxes):
        a.grid(column=idx,row= 0)
    for i in ziektes:
        Listboxes[1].insert('end', i)
    

    #maak Koppeling button
    Label_variable = StringVar()
    def maak_koppeling():
        nonlocal Label_variable
        if Listboxes[0].curselection() and Listboxes[1].curselection():
            
            Label_variable.set(f"U heeft gekozen voor {gekozen_artsen[Listboxes[0].curselection()[0]]} voor een behandeling voor {ziektes[Listboxes[1].curselection()[0]]}.")
            
            Label(Label_frame , text=Label_variable.get()).pack()
        else:
            messagebox.showwarning("Warning!","You haven't chosen both options, please try again.")
            
    button = Button(Listbox_frame,text="Maak koppeling", command=maak_koppeling)
    button.grid(column=0,row=1)
    
    
    #lable'
    Label_frame = Frame(root)
    Label_frame.pack()
    
    

#Opdracht van les 6
'''    from tkinter import messagebox
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














    root.mainloop()'''