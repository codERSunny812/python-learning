# parent class 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# child class

# if you have used the init inside the child class  so it will override the parent class to avoid this you can do this add a call to the parent init function from the child init function

class Student(Person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationYear = year
  

  def intro(self):
    print("welcome",self.firstname,self.lastname,"to the class of",self.graduationYear)




y = Student("sunny","pandey",2019)  # here we are accessing the method and properteis of the parent class from a child class
y.printname()
y.intro()



