#if statement = a block of code that will execute if it's condition is true

age = int(input("How old are you?"))

if age >= 69:
    print("You are too old!")

elif age >=18:
    print("You are an adult!")

elif age<0:
    print("You haven't been born yet!")
else:
    print("You are a child!")