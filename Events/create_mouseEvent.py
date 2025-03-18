from tkinter import *

def doSomething(event):
    print("Mouse Coordinates" +str(event.x)+" "+str(event.y))

window = Tk()

#window.bind("<Button-1>",doSomething)       #left mouse click
#window.bind("<Button-2>",doSomething)       #scroll wheel
#window.bind("<Button-3>",doSomething)       #right mouse click
#window.bind("<ButtonRelease>",doSomething)       
#window.bind("<Enter>",doSomething)           #Enter the window
#window.bind("<Leave>",doSomething)           #Leave the window
window.bind("<Motion>",doSomething)

window.mainloop() 