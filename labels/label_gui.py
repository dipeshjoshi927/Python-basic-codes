# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()
#window.config(background="black")
#window.geometry("420x420")

photo = PhotoImage(file='person.png')

label = Label(window,
              text="Hello Bitches!!",
              font=('Arial',20,'italic'),
              fg='#00FF00',
              bg='grey',
              relief=RAISED,
              bd=100,
              padx=20,
              pady=20,
              image=photo,
              compound='left')
label.place(x=50,y=50)
label.pack()

window.mainloop()