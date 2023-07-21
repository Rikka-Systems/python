# Print function python

name = "Jason"
occupation = "God"
age = 41

# f string
print(f'1. {name} is a {occupation} and he is {age} years old')

# format
print("2. {} is a {} and he is {} years old".format(name, occupation, age))

# Sperating multiple arguments
print("3.", name, "is a", occupation, "and he is", age, "years old")
print("4.", name, "is a", occupation, "and he is", age, "years old", sep="|||")

# String Concat

# the wrong way. age is typed as an int not str
# print("5. " + name + " is a " + occupation + " and he is " + age + " years old")

# the right way. age is read as an int not an str. The original type is unchanged
print("5. " + name + " is a " + occupation + " and he is " + str(age) + " years old")
print(type(age))

# the old way
print("First name: %s Last Name: %s Int: %i Float %f" % ("Jason", "X", 10, 20.5))
