thisIsSet = {"apple", "banana", "cherry"}

print(thisIsSet)


# addding the values in the set

thisIsSet.add("orange")
print(thisIsSet)

# to add another set or multiple values we use update method

thisIsSet.update({"sunny","sumit"})

print(thisIsSet)


# removing items from the set

thisIsSet.remove("sumit")

thisIsSet.discard("banana")

thisIsSet.pop() # remove item randomly

print(thisIsSet)


# looping  throught the set

for items in thisIsSet:
    print(items)


# methods in sets

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}


# 1. Union ( new set is returned) 

print(set1.union(set2)) 

# 2. Intersection ( new set is returned)
print(set1.intersection(set2))


# 3. updates (modifies the original set)
set1.update(set2)
print(set1)

# 4. Intersection update (modifies the original set)
set1.intersection_update(set2)
print(set1)

# 5. Difference ( new set is returned)
print(set1.difference(set2))

# 6. Difference update (modifies the original set)

set1.difference_update(set2)
print(set1)


#  frozen set 

frozenSet = frozenset([1,2,3,4,5])
print(frozenSet)
