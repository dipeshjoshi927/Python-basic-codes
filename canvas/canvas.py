# canvas = widget that is used to draw graphs, plots, images in window

from tkinter import *

window = Tk()

canvas = Canvas(window,height=500,width=500)
#canvas.create_line((0,0),(500,500),fill="grey",width=5)
#canvas.create_line((0,500),(500,0),fill="black",width=5)
#canvas.create_rectangle((50,50),(250,250),fill="purple")
#points = [(250,0),(500,500),(0,500)]
#canvas.create_polygon(points,fill="sky blue",outline="grey",width=5)
#canvas.create_arc(0,0,500,500,fill="light green",style=PIESLICE,start=90,extent=180)

canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_oval(190,190,310,310,fill="grey",width=10)

canvas.pack()

window.mainloop()