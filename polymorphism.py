class Animals:
    def move(self):
        print("Animal is moving")
class Dog(Animals):
    def move(self):
        print("Dog is running")
class Cat(Animals):
    def move(self):
        print("Cat is walking")
class Fish(Animals):
    def move(self):
        print("Fish is swimming")
class Vehicles:
    def move(self):
        print("Vehicle is moving")
class Car(Vehicles):
    def move(self):
        print("Car is driving")
class Plane(Vehicles):
    def move(self):
        print("Plane is flying")
class Boat(Vehicles):   
    def move(self):
        print("Boat is sailing")