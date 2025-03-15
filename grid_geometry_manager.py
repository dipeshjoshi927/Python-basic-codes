#grid() = geometry manager that organizes widgets in a table-like structure in a parent 

from tkinter import *

window = Tk()

titleLabel = Label(window,text="Enter your window",font=("Arial",20)).grid(row=0,column=0,columnspan=2)
firstNameLabel = Label(window,text = "First Name: ",width=20,bg="grey").grid(row=1,column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text = "Last Name: ",width=30,bg="cyan").grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailLabel = Label(window,text = "Email: ",width=10,bg="magenta").grid(row=3,column=0)
emailEntry = Entry(window).grid(row=3,column=1)
submitButton = Button(window,text = "submit").grid(row=4,column=0,columnspan=2)

window.mainloop()