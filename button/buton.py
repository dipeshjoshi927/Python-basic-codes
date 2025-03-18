# button = you click it, then it does stuff

from tkinter import *

window = Tk()
window.geometry("420x420")
window.config(background="black")

icon = PhotoImage(file='like.png')

count = 0

def click():
    global count 
    count += 1
    print(count)


button = Button(window,
                text="CLICK",
                command = click,
                font=('Comic Sans',20),
                fg="#00FF00",
                bg='grey',
                activeforeground="#00FF00",
                activebackground="grey",
                state=ACTIVE,
                image=icon,
                compound = "top"
                )
button.pack()
window.mainloop()
