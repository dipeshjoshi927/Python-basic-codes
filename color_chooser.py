from tkinter import *
from tkinter import colorchooser  #submodule

def click():
    color = colorchooser.askcolor()
    window.config(bg = color[1])       #changes background color

window = Tk()
window.geometry("420x420")
button = Button(window,text="CLICK",command=click)
button.pack()
window.mainloop()