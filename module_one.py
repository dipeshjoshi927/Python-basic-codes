#-------------------------------------
# if __name__ == '__main__'
#-------------------------------------

# y tho?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other module

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__


def hello():
    print("HEllo")

if __name__ == '__main__':
    hello()
else:
    print("runing this module indirectly")
    






