s = {"Hallo", "Welt"}
print(s)

s.add("Mars")
print(s)

s.add("Mars")
print(s)


text = "Hallo Welt Hallo Mars Hallo Welt"
words = set()
for w in text.split(" "):
    words.add(w)

print(words)
print(len(words))



my_set = {i for i in range(10)}
print(my_set)