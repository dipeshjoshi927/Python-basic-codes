from tkinter import *

def function(event):
    #print("You pressed " ,event.keysym)
    label.config(text=event.keysym)
window = Tk()

window.bind("<Key>",function)

label = Label(window,font=("helvetica",19))
label.pack()

window.mainloop()