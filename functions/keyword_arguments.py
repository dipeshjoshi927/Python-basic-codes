#keyword arguments = arguments preceded by an identifier when we pass them to a function
#                    The order of the argument doesn't matter, unlike positional argument
#                    Python knows the names of the argument that our function receives

def hello(first,middle,last):
    print("Hello " +first +" " +middle + " "+last)

hello(last="joshi",middle="prasad",first="Dipesh")   
