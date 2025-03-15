### while loop = a statement that will execute it's block of code,
#             as long as it's condition remains true

#while 1==1:
 #   print("I'm stuck in a loop")

#name =""
#while len(name) == 0:
 #   name = input("Enter your name!!")
  #  print("Hello " ,name)



### for loop = a statement that will execute it's block of code 
#              a limited amount of times
#      while lopp = unlimited 
#       for loop = limted


#for a in range(10):
 #   print(a+1)

#for b in range(50,100,5):
 #   print(b)

#for a in "Dipesh Joshi":
    
 #   print(a)

#for seconds in range(0,10,+2):
 #   print(seconds)
    
#print("Happy new year!")


### nested loop = The "inner loop" will finish all of it's iterations before 
#                 finishing one iteration of the "outer loop"

rows = int(input("Enter number of rows:"))
columns = int(input("Enter number of columns:"))
symbol = input("Enter the symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="" )
    print()

