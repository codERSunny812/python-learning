## diffrent classes have same method:

class Car:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move():
        print("drive")



class Boat:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move():
        print("sail")



class Plane:

    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move():
        print("fly")



# creating the object of the classes 

car1 = Car("Ford","Mustang")

boat1 = Boat("Ibiza","touring 20")

plane1 = Plane("boeing","747")



for x in [car1,boat1,plane1]:
    x.move()