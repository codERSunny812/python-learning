class Person:

    # class properties 
    def __init__(self,name,age=None,city=None):
        self.name=name
        self.age=age
        self.city=city

    def selfIntro(self):
        print(self)



p1 = Person("sunny")
print(p1.name) # accessing  property
# p1.selfIntro()

# modifying property
p1.name="prathistha"

print(p1.name)

p2= Person("bunny",24)
# p2.selfIntro()

print(p2.name)
print(p2.age)

# del p2.age
# print(p2.age)  # will raise attribute error


p3= Person("chunny",22,"pune")
# p3.selfIntro()


# class properties 

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

p1.species = "Alien"  # Modifying instance property

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)


class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))


