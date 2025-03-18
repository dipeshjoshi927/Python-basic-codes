from tkinter import *

window = Tk()

x = IntVar()
icon = PhotoImage(file="pyhon.png")

def display():
    if(x.get()==1):
        print("I agree!!")
    else:
        print("I don't agree!!")

check_button = Checkbutton(window,
                           text="I agree with the statement",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=("Arial",20),
                           bg="black",
                           fg="#00FF00",
                           activebackground="grey",
                           activeforeground="#00FF00",
                           padx=10,
                           pady=10,image = icon,
                           compound="left"
                           )
                          
check_button.pack()



window.mainloop()