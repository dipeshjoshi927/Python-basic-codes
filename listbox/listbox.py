# listbox = A listbox of selectable text items within it's own container

from tkinter import *

window = Tk()

def submit():
    print("The choices you selected are: ")
    for i in listbox.curselection():
        print(listbox.get(i))

def add():
    listbox.insert(listbox.size(),entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    listbox.config(height=listbox.size())

listbox = Listbox(window,
        bg="#f7ffde",
        font=("helvetica",35),
        width=12,
        selectmode='multiple')
listbox.pack()

listbox.insert(1,"pizza",)
listbox.insert(2,"pasta",)
listbox.insert(3,"garlic bread",)
listbox.insert(4,"soup",)
listbox.insert(5,"salad",)

listbox.config(height=listbox.size())

entrybox = Entry(window)
entrybox.pack()

submitbutton = Button(window,text= "Submit",command= submit)
submitbutton.pack()

addbutton = Button(window,text= "Add",command= add)
addbutton.pack()

deletebutton = Button(window,text= "Delete",command= delete)
deletebutton.pack()
window.mainloop()