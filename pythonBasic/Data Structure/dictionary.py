thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# acccesing the dictionary items

print(thisdict["brand"])

print(thisdict.get("model"))

# to  get the keys
x = thisdict.keys()
print(x)
# to get the values
y = thisdict.values()
print(y)

# to get the items
z = thisdict.items()
print(z)


# changing values in dictionary
thisdict["year"] = 2020
print(thisdict)

thisdict.update({"model":"Focus"})
print(thisdict)

# adding items in dictionary
thisdict["color"] = "red"
print(thisdict)


# removing items from dictionary
thisdict.pop("model")
print(thisdict)
thisdict.popitem()  # removes the last inserted item
print(thisdict)


# looping through the dictionary

print("Looping through dictionary:234567856784567845678456789")
for key in thisdict:
    # print(key)
    print(thisdict[key])


print("Looping through dictionary keys and values:")


# copying the dictionary
mydict = thisdict.copy()
print(mydict)


# nested dictionary 

myFamily={
    "child1":{
        "name":"Emil",
        "year":2004
    },
    "child2":{
        "name":"Tobias",
        "year":2007
    },
    "child3":{
        "name":"Linus",
        "year":2011
    }
}

print(myFamily)

# accessing items in nested dictionary
print(myFamily["child2"]["name"])

print(myFamily.items())

# looping through nested dictionary

print("Looping through nested dictionary:")

for x,y in myFamily.items():
    for i,j in y.items():
        print(i,j)
