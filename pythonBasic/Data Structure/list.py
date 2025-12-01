# creation of list 
list1 = [1, 2, 3, 4, 5]
print(list1)

list2 = list([6, 7, 8, 9, 10])
print(list2)

# accessing elements
print(list1[1:4])

# checking element exist in the list or not

if 3 in list1:
    print("3 is present in the list")
else:
    print("3 is not present in the list")


# change the list  element 

list1[2]=55
print(list1)

# adding element in the list

list1.append(99) # at the end of the list
print(list1)

list1.insert(2,76) # at specific position
print(list1)

list1.extend([100, 101, 102]) # adding multiple elements
print(list1)

# removing element from the list

list3 = [1,2,2,2,3,4,54,67,98]
print(list3)

list3.remove(2) # remove the first occurence of the element
print(list3)

list3.pop() # remove the last element fromt the list
print(list3)


# to clear the list 
list3.clear()
print(list3)


# looping in the list 

for item in list2:
    print(item)

thisIsList = ["apple", "banana", "cherry"]

for i in range(len(thisIsList)):
    print(thisIsList[i])





# sorting the list

unsortedList = [5,3,8,6,7,2,4,1]
unsortedList.sort()
print(unsortedList)
unsortedList.sort(reverse=True)
print(unsortedList)

# copying the list

copiedList = unsortedList.copy()
print(copiedList)

copiedList2 = list(unsortedList)





