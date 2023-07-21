# Lists

# define a list
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

# Access
print(fruits[1])

# Negative index
print(fruits[-1])

print(fruits[-2])

# Count of items. Case-sensitive
print(fruits.count("apple"))

print(fruits.count("tangerine"))

# Where is an item
print(fruits.index("banana"))

print(fruits.index("banana", 4))

# Reverse order
fruits.reverse()
print(fruits)

# Append
fruits.append("grape")
print(fruits)

# Insert
fruits.insert(3, "mango")
print(fruits)

# Sort alphabetically
fruits.sort()
print(fruits)

# Remove last item
fruits.pop()
print(fruits)

# Loop thru list
for x in fruits:
	print(x)

# Check for item in list
if "apple" in fruits:
	print("Yes")

print("apple" in fruits)

# slice a list. end index = start index + number of items to return
print(fruits)
print(fruits[3:6]) # returns 3 items starting at index 3
print(fruits[4:]) # returns all items starting at index 4 to the end
print(fruits[-4:-2])

# delete an item. Only deletes first instance of item
fruits.remove("kiwi")
print(fruits)
