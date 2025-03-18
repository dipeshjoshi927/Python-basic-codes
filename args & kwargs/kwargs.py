# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword argument


def hello(**kwargs):
    print("Hello "+ kwargs['first'] + " "+ kwargs['last'])
    print("Hello",end=" ")
    for keyword,value in kwargs.items():
        print(value,end=" ")


hello(first="Mr.",second="Dipesh",third="Dude",last="Joshi")   

