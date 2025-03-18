from tkinter import *

def openFile():
    print("File has been opened")
def saveFile():
    print("File has been saved ")

def cut():
    print("you cut some text")
def copy():
    print("you copied some text")
def paste():
    print("you pasted some text")


window = Tk()
openImage = PhotoImage(file='open.png')
saveImage = PhotoImage(file='save.png')
exitImage = PhotoImage(file='exit.png')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command= openFile,image=openImage,compound='left')
fileMenu.add_command(label="Save",command= saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')


editMenu = Menu(menubar,tearoff=0,font=("MV Boli",10))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command= cut)
editMenu.add_command(label="Copy",command= copy)
editMenu.add_command(label="Paste",command= paste)

window.mainloop()