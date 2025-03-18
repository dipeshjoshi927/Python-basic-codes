# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created.

name = "Dipesh"# global scope (available inside and outside function)

def display_name():
    name = "Dipesh"   #local scope(available only inside this function)
    print(name)
display_name()        #for local scope


print(name)          # for global scope

# L = local
# E = Enclosing 
# G = Global
# B = Built-in