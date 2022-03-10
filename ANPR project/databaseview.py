from tkinter import *
import tkinter.ttk as ttk

import sqlite3

def DisplayForm():
    display_screen=Tk()
    display_screen.geometry("400x400")

    display_screen.title("ANPR_PROJECT")
    global tree
    global SEARCH
    SEARCH=StringVar()

    TopViewForm = Frame(display_screen, width=300, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(display_screen, width=200)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(display_screen, width=200)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="SQLite Database for ANPR ", font=('verdana', 18), width=600,bg="#1C2833",fg="white")
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('verdana', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)


    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_search = Button(LeftViewForm, text="View All", command=DisplayData)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)

    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("date_time", "num"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('date_time', text="Date and Time", anchor=W)
    tree.heading('num', text="Numbers", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)

    tree.pack()
    DisplayData()

def SearchRecord():
    if SEARCH.get() !="":
        tree.delete(*tree.get_children())
        conn=sqlite3.connect('number.db')
        cursor=conn.execute("SELECT * FROM numbers WHERE num LIKE?",('%'+str(SEARCH.get())+'%',))
        fetch=cursor.fetchall()

        for data in fetch:
            tree.insert('','end',values=(data))
        cursor.close()
        conn.close()

def DisplayData():
    tree.delete(*tree.get_children())
    conn=sqlite3.connect('number.db')
    cursor=conn.execute("SELECT * FROM numbers")
    fetch=cursor.fetchall()
    for data in fetch:
        tree.insert('','end',values=(data))
    cursor.close()
    conn.close()
    
DisplayForm()
if __name__=='__main__':
#Running Application
 mainloop()       
        








    
