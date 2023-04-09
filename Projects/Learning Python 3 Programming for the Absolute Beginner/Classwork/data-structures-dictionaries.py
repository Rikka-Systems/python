movie = {
	"title": "Inception",
	"rating": "PG-13",
	"director":"Christopher Nolan",
	"stars":["Leo DiCap", "Tom Hardy"]
}

# Extraction

print(movie["title"])
print(movie["stars"][1])

# Change value

movie["rating"] = "R"

# Add

movie["runtime"] = 200

print(movie)

# Looping Dictionary

for x in movie:
	print(x)

for x in movie:
	print(movie[x])

for x, y in movie.items():
	print(x, y)

# Check for key

if "rating" in movie:
	print("Yep")

# remove items

movie.pop("rating")
print(movie)

# clear

movie.clear()
print(movie)

# delete the entire dictionary (free memory)

del movie
