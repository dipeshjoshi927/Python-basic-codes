#Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")

class Bike(Vehicle):
    def go(self):
        print("You ride the bike")
    def stop(self):
        print("This bike is stopped")



car = Car()
bike = Bike()


car.go()
bike.go()
car.stop()
bike.stop()