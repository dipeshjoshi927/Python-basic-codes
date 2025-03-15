from tkinter import *
from tkinter import ttk

window = Tk() 

notebook = ttk.Notebook(window)     #widget that manages a collection of windows/displays

tab1 = Frame(notebook)     #new frame for tab1
tab2 = Frame(notebook)     #new frame for tab1

notebook.add(tab1,text="tab1")
notebook.add(tab2,text="tab2")
notebook.pack(expand=True,fill="both")      # expand = expand to fill any space not otherwise used
                                 # fill = fill space on x and y axis

Label(tab1,text="Hello, this is tab-1",width=25,height=25).pack()
Label(tab2,text="Hello, this is tab-2",width=20,height=20).pack()

window.mainloop()