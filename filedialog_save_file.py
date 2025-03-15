from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="D:\\CODING\\Prolog",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All file", ".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get("1.0",END))
    #filetext = input("Enter some text")
    file.write(filetext)
    file.close()

window = Tk()



button=Button(window,text="Save",command = saveFile)
button.pack()

text = Text(window,bg='light yellow',font=("Ink Free",12),height=12,width=20)
text.pack()
window.mainloop()
