from car import Car

car_1 = Car("Chevy","Corvette",2021,"Blue")
car_2 = Car("Ford","Mustang",2022,"Royal Red")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

Car.wheels = 2 #without it, it'll print 4 which is declared in class variable 
print(car_1.wheels)
car_1.drive()
car_2.stop()