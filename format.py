# str.format() = optional method that gives users
#                more control when dispaying output

animal = "cow"
item = "moon"

print("The "+animal+" "+ "jumped over the "+item)
print("The {} jumped over the {}".format(animal,"moon"))
print("The {1} jumped over the {0}".format(animal,item)) #posiional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

#name = "Dipesh"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}.Nice to meet you.".format(name))
#print("Hello, my name is {:<10}.Nice to meet you.".format(name))
#print("Hello, my name is {:>10}.Nice to meet you.".format(name))
#print("Hello, my name is {:^10}.Nice to meet you.".format(name))




number = 1000000000000

print("The number pi is {:.2f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))

