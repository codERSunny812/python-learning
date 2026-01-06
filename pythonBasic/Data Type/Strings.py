name = "sunny" # normally declared a string

name = str("sunny") # declared using str() constructor  

print("name:", name)

name = """ hello this is sunnny  and 
this is a multi line string """


# accsessing string characters using indexing

first_char  = name[0]
print(first_char)

# looping throught a string 

str = "sunny"


print("----using for loop ----")

for x in str:
    print(x)


print("----using range() function ----")

for i in range(len(str)):
    print(str[i])



# string slicing 

str = "Hello, welcome to sunny's world"

print(len(str))
print(str[0:5])  # prints 'Hello'
print(str[7:14]) # prints 'welcome'
print(str[15:])  # prints 'to sunny's world'
print(str[-9:-1]) # using the negative indexing 


# string in  python 

a = "    Helllooo hoooman being         "

print(a.upper())
print(a.lower())
print(a.strip()) # remove the white spaces
print(a.replace("Helllooo", "Hola amigo")) 
print(a.split(" ")) # splits the string into a list


# formating the string 

age = 23
name = "sunny"

print(f"my name is {name} and my age is {age}.")


def welcome(name, age):
    return f"my name is {name} and my age is {age}.".format(name=name, age=age)


print(welcome("sushil", 25))


print(str.count("o")) 