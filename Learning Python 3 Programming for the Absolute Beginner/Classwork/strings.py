# Strings

a = "Hello"
print(a)

# Multiline strings
a = """this is a multiline string in
python. You cna use this method
if there is a lot of information you want
to assign to a string"""
print(a)

a = '''this is a multiline string in
python. You cna use this method
if there is a lot of information you want
to assign to a string'''
print(a)

# Strings are arrays
a = "Hello, World!"
print(a[1])

# Slicing
b = "Hello, World!"
print(b[2:5])

# Negative indexing
print(b[-5:-2])

# String length
print(len(b))

# Methods

# Strip
a = " Hello, world! "
print(a.strip())

# Convert case
print(a.lower())
print(a.upper())

# Replace (Case sensitive)
print(a.replace("H", "J"))

# Split (Delimiter is 'eaten'?)
print(a.split(","))

# In
txt = "The rain in spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Find
txt = "It is a great day to learn python"
print(txt.find("great"))

# Is numeric
txt = "1250"
print(txt.isnumeric())

# Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# Format
age = 41
txt = 'My name is Jason, and I am {}'
print(txt.format(age))

print(f'My name is Kevin and I am {age} year older than my girl friend')

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}"
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay ${2} for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))
