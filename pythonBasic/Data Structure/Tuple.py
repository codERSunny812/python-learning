thisIsTuple = ("sunny","sumit","sushil","sachin")
print(thisIsTuple)

# accesssing  the tuple items 

print(thisIsTuple[1])
print(thisIsTuple[-1])

# adding items to tuple

# we can't add items to tuple directly as tuple is immutable but we can concatenate two tuples to add items or we can convert tuple to list and add items to it and then convert it back to tuple.


thisIsTuple = thisIsTuple + ("newItem",)
print(thisIsTuple)

# unpacking of  the tuple 

colors = ("red","green","blue")
(color1, color2, color3 )= colors

print(color1)
print(color2)
print(color3)


# looping through the tuple

for item in thisIsTuple:
    print(item)


#looping  throught  index number

for i in range(len(thisIsTuple)):
    print(thisIsTuple[i])

# methods in tuples
print(thisIsTuple.count("sushil"))  # counts the occurence of the item in the tuple
print(thisIsTuple.index("sumit"))   # returns the index of the item in the

