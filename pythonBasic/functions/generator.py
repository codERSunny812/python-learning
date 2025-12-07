def basic_generator():
    yield 1
    yield 2
    yield 3 
    yield 4
    yield 5


for value in basic_generator():
    print("Generated value:", value)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1


for num in count_up_to(5):
  print(num)