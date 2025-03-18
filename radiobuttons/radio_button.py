# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

window = Tk()

def order():
    if(x.get() == 0):
        print("you ordered pizza!")
    elif(x.get() == 1):
        print("you ordered burger!")
    elif(x.get()==2):
        print("you ordered hotdog!")
    else:
        print("huh?")

pizzaImage = PhotoImage(file='pizza.png')
burgerImage = PhotoImage(file='burger.png')
hotdogImage = PhotoImage(file='hotdog.png')
foodImages =[pizzaImage,burgerImage,hotdogImage]
x = IntVar()
food = ["Pizza","Burger","HotDog"]

for i in range(len(food)):
    radio_button = Radiobutton(window, 
                                text=food[i],      #adds text to radio buttons
                                variable = x,      #groups radiobuttons together if they share the same variable
                                value = i ,        #assigns each radiobutton a different value 
                                padx = 25,         #adds padding on x-axis
                                pady = 25,
                                font = ("Impact", 20),
                                image = foodImages[i], #adds image to radiobuttons
                                compound = 'left',     #adds image & text(left-size)
                                indicatoron=0,         #eliminate circle indicators         
                                width = 375,           #sets width of radio button
                                command=order)         #set command of radio button to radio button 
    radio_button.pack(anchor='w')



window.mainloop()