# getting types

# string
x = "Hello world"
print(type(x))

# int
x = 10
print(type(x))

# float
x = 20.5
print(type(x))

# list
x = ["apple", "banana", "orange"]
print(type(x))

# dictionary
x = {"name": "John", "age": 34}
print(type(x))

# set
x = {"apple", "banana", "orange"}
print(type(x))

# bool
x = True
print(type(x))

# bytearray
x = bytearray(5)
print(type(x))

# memoryview
x = memoryview(bytes(5))
print(type(x))

# Setting type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = list(("apple", "banana", "orange"))
x = tuple(("apple", "banana", "orange"))
x = dict(name="Jason", age=41)
x = set(("apple", "banana", "orange"))
x = frozenset(("apple", "banana", "orange"))
x = bool(5)

# Convert
x = 1 # Int
y = 2.3 # Float

# int2float
a = float(x)

# float2int
b = int(y)

# Casting
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x, type(x), y, type(y), z, type(z), w, type(w))

x = str("s1")
y = str(2)
z = str(3.0)

print(x, type(x), y, type(y), z, type(z))