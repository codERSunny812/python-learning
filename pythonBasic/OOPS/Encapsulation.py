class Person:

    def __init__(self,name,age):
        self.name=name
        self.__age=age


    def personIntro(self):
        print("My name is",self.name,"and my age is",self.__age)
    
    # to access the private property we have to use the getter function

    def get_age(self):
        return self.__age
    
    # to change the  value of the  private property we  have to use the setter function

    def set_age(self,age):
        if age > 0:
            self.__age=age
        else:
            print("age is already  postive")

        
    


p1 = Person("sunny",25)
p1.personIntro()
print(p1.name)
#print(p1.__age) # error occured
print(p1.get_age())
p1.set_age(-1)
print(p1.get_age())
