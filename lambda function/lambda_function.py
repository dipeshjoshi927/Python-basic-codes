# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time,throw-away )

# syntax--> lambda parameters:expression

def double(x):
    return x*2

print(double(10))

#This can be written as 
double = lambda x:x*2
print(double(5))

multiply = lambda x,y:x*y
print(multiply(5,6))

add = lambda x,y,z:x+y+z
print(add(1,2,3))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Dipesh","Joshi"))

age_check = lambda age:True if age>=18 else False
print(age_check(20))