# Tuples

# Define a tuple
fruit = ("apple", "banana", "cherry", "orange", "grapes", "nectarine")
print(fruit)

# Access element
print(fruit[1])

# Slice
print(fruit[2:5])

# Change tuple values
fruit = list(fruit)
print(fruit)
fruit[1] = "guava"
fruit = tuple(fruit)
print(fruit)

# Loop thru tuple
for x in fruit:
	print(x)

# Check for item
if "apple" in fruit:
	print("yes it is")

# join
veggies = ("carrots", "squash")
produce = fruit + veggies
print(produce)

# Named
from collections import namedtuple
person = namedtuple("Person", "name age gender")
user = person(name="Fred", age=34, gender="male")
print(user)
print(user.name)
print(user.age)
print(user.gender)
