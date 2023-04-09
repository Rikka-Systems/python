# 1
input = "The weather is great today"
vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

for x in input:
    if x in ["a", "e", "i", "o", "u"]:
        vowels[x] += 1

print(vowels)
print("a = {}".format(vowels["a"]))
print("e = {}".format(vowels["e"]))
print("i = {}".format(vowels["i"]))
print("o = {}".format(vowels["o"]))
print("u = {}".format(vowels["u"]))

for index in sorted(vowels):
    print(index, ":", vowels[index])

# 2
sentence = "There has never been a better time to learn Python"
words = sentence.split()
words.reverse()
print(words)
print(" ".join(words))
