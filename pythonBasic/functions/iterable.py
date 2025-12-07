listt = list([1, 2, 3, 4, 5])

my_iter = iter(listt)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5
# print(next(my_iter))  # This would raise StopIteration error  