#Variables in Python
#no command for declaring a variable

x = 10
name = "Jason"

print(x)
print(name)

#Assigning a value to multiple variables
fruit1, fruit2, fruit3 = "apple", "orange", "banana"
print(fruit1)
print(fruit2)
print(fruit3)

#Output variables
name = "jason"
print("Hello" + " " + name)

#Global variables

x = 20

def addition():
    #local variables
    x = 10 + 30
    print(x)

addition()

print (x)
