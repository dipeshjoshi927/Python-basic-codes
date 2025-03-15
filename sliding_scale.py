from tkinter import *

def submit():
    print("The temperature is: ",str(scale.get()),"C")

window = Tk()

hotimage = PhotoImage(file='fire.png')
hotlabel = Label(image=hotimage)
hotlabel.pack()

scale = Scale(window,
              from_ = 100,to=0,
              length = 500,
              orient= VERTICAL,             #orientation of scale
              font = ('Consolas',20),       
              tickinterval=10,              #adds numeric indicators for value
              #showvalue=0,                 #hide current value
              #resolution=5,                #increment of slider
              troughcolor="pink",
              fg="red",
              bg="black",
              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])      #set current value of slider
scale.pack()

coldimage = PhotoImage(file='cold.png')
coldlabel = Label(image=coldimage)
coldlabel.pack()

button = Button(window,text="Submit", command = submit )
button.pack()



window.mainloop()