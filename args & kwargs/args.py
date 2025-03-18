# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of argument

def add(*args):
    sum = 0
    args = list(args) #tuple cannot be changed so we make it a list
    args[0]=0 
    for i in args:
        sum += i
    return sum

print (add(1,2,3,4))  