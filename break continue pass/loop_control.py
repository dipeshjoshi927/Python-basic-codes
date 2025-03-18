#loop control statement = change a loops execution from it's normal sequence
#  break =    used to terminate the loop entirely 
# continue =  skips to the next iteration of the loop 
# pass =      does nothing, acts as a placeholder


while True: 
    name = input("Enter your name!:")
    if name != "":
        break 
print ("Hello ",name)    
    
phone_number = "123-234-567-769"      

for i in phone_number:
    if i == "-":
       continue
    print(i, end="")


for i in range(1,21):
     if i == 13:
        pass
     else:
        print(i,end=" ")
        


