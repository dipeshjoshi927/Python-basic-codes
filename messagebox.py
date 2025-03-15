from tkinter import *
from tkinter import messagebox

def click():
        # messagebox.showinfo(title='This is an info ',message="You bitch")
#------------------------------------------------------------------------------------------------------      
          #messagebox.showerror(title="Error",message="something went wrong")
#------------------------------------------------------------------------------------------------------      
      #messagebox.showwarning(title='Warning ',message="You have a virus")
#------------------------------------------------------------------------------------------------------      
        #if messagebox.askokcancel(title='ask ok cancel',message='do you want to do the thing?'):
         #       print("You did a thing!")
        #else:
        #        print("You didn't do a thing!")
#------------------------------------------------------------------------------------------------------      
       #if messagebox.askretrycancel(title='ask retry cancel',message='do you want to retry the thing?'):
         #      print("You retried a thing!")
        #else:
          #      print("You didn't retry a thing!")
#------------------------------------------------------------------------------------------------------      
          #if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
         #       print("I love cake too!")
        #else: 
         #       print("More cake for me!")
#------------------------------------------------------------------------------------------------------      
        #answer = messagebox.askquestion(title = 'ask question', message='Do you like pie')
        #if(answer=='yes'):
        #        print('I like pie too')
        #else:
        #        print('More pie for me!')
#------------------------------------------------------------------------------------------------------      
        answer = messagebox.askyesnocancel(title='YES NO CANCEL',message='Do you like to code?',icon='warning')
        if(answer==True):
                print("I love coding too!")
        elif(answer==False):
                print("More coding for me!")
        else:
                print("Maybe later...")

window = Tk()

button = Button(window,text="CLICK HERE",command = click)
button.pack()

window.mainloop()