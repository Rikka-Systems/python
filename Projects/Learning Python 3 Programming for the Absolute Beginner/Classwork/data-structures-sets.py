# Sets

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Access
for x in fruits:
	print(x)

# Add 1 item
fruits.add("orange")
print(fruits)

# Add multiple
fruits.update(["mango", "kiwi", "strawberry"])
print(fruits)

# Get length
print(len(fruits))

# Remove item. Error if you try to remove an item that is not present
fruits.remove("kiwi")
print(fruits)

# Discard item. No error if you try to remove an item that is not present
fruits.discard("blueberry")

# Empty a set
fruits.clear()
print(fruits)

# Join 2 sets. Declare new set to hold union
veg = {"carrots", "squash"}
fruits = {"apple", "banana", "cherry"}
produce = fruits.union(veg)
print(produce)

# Update. Updates existing set
set1 = {"a", "b", "c", "d"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
print(set2)

# Frozen set. Unable to change the set
names = frozenset(["Jim", "John", "Mike"])
print(names)

names.remove("Jim")
print(names)








