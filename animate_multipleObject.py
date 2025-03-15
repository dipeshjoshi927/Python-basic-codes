from tkinter import *
from Ball import *
import time 

window = Tk()
window.title("Bouncing ball")

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volly_ball = Ball(canvas,0,0,100,1,1,"blue")
tennis_ball = Ball(canvas,0,0,10,2,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,5,"orange")

while True:
    volly_ball.move()
    tennis_ball.move()
    basket_ball.move() 
    window.update()
    time.sleep(0.01)

window.mainloop()