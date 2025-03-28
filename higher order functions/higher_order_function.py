# Higher order function = a function that either:
#                         1. accepts a function as an argument
#                         2. returns a function
#                         (In python, function are also treated as objects)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)

hello(loud)
hello(quiet)
#***********************************************

def divisor(x):
    def dividend(y):
        return y / x
    return dividend

divide = divisor(2)
print(divide(10))

