# Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
# Tk() = new independent window

from tkinter import *

def create_window():
    new_window = Tk()
    #new_window = Toplevel()
    old_window.destroy()      #closes out of old window

old_window = Tk()

Button(old_window,text="Create new window",command=create_window).pack()

old_window.mainloop()