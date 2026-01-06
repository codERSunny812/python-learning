# basic function creation and usage

# def my_function():
#   print("Hello from a function")


# my_function()

# # if you dont know how many arguments will be passed

# def my_function(*kids): # kids is a tuple here
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# def my_function(**kid): # kids is a dictionary here
#   print(kid)
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())

# # decorators in python 

# def decor_fun1(func):
  
#   def decor_innner():
#     return func().upper()
  
#   return decor_innner


# @decor_fun1
# def myFunc():
#   return "hello world"

# print(myFunc())

# # by placing tge @decor_fun1 above the function definition of myFunc, the function is being decorated with decor_fun1. This means that when myFunc is called, it is actually calling the inner function decor_innner defined within decor_fun1, which modifies the output of myFunc to be in uppercase.



# multiple decor function 

# def changecase(func):
#   def myinner():
#     return func().upper().count("A")
#   return myinner

# @changecase
# def myfunction():
#   return "Helaaa amigooooaaoaoao"

# @changecase
# def otherfunction():
#   return "I aaaaaam speed!"

# print(myfunction())
# print(otherfunction())


# # argument in the decorator function 

# def changecase2(func):
#   def myinner2(x):
#     return func(x).upper()
#   return myinner2

# @changecase2
# def myfunction2(nam):
#   return "Hello " + nam

# print(myfunction2("John"))


# Decorators can accept their own arguments by adding another wrapper level.


def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(10)
def myfunction():
  return "HellA LiNuS"

print(myfunction())


# we can use multiple decorators  on a single function 

# lambda function 

print("\n Lambda function \n")


# function that adds 3 numbers

add = lambda x,y,z : x+y+z

print(add(5,6,7))



# function to square a number

def myfunc(n):
  
  return lambda a:a**n


result = myfunc(4)


print(result(2))