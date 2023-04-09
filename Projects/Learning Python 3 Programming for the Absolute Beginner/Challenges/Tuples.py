n = 10
my_tups = [(12, 3, 10), (5, 3), (11, 10, 90), (12, 13, 51)]

for x in my_tups:
	if n not in x:
		my_tups.pop(my_tups.index(x))

print(my_tups)
