class Car:
    color = None 

class Motocycle:
    color = None

def change_color(vehicle,color):
    vehicle.color = color

car1 = Car()
car2 = Car()
car3 = Car()
bike1 = Motocycle()

car1.color = "blue"

change_color(car1,"yellow")
change_color(car2,"orange")
change_color(car3,"brown")
change_color(bike1,"red")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)