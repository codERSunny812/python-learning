# creating a  basic class 

class Person:

    name = "sushil"
    age = 24
    city = "pune"
    def greet(self):
        print("hello , good morning")


# creating object of class

p1 = Person()
print(p1.name)
print(p1.age)
print(p1.city)
p1.greet()

# deleting object
del p1


# all class have a method called __init__ , which is used to initialize the object of class

class PersonInfo:

    def __init__(self,name,age,city,gender):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender

    def info(self):
        print(f"Name is {self.name} , age is {self.age} , city is {self.city} and gender is {self.gender}")


# creating object of class
p2 = PersonInfo("sushil",24,"pune","male")
print("Hey there! I'm person 2 , here is my info:")
p2.info()
p3=PersonInfo("prathistha",22,"delhi","female")
print("Hey there! I'm person 3 , here is my info:")
p3.info()