a = 33
b = 200
if b > a:
  print("b is greater than a")

# we can have multiple print statements in if block
if b > a:
  print("b is greater than a")
  print("This is inside if block")  

# elif statement 

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")