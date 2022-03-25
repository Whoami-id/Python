#types for key: boo, int, float, str, tuple, None (Immutable type)

d = {"Berlin": "BER", "Helsinki": "HEL", "Saigon": "SNG"}

print(d)

print(d["Helsinki"])
print(d.get("Saigon"))


d["Budapest"] = "BUD"
print(d)

del d["Budapest"]
print(d)

if "Budapest" in d:
    print("Budapest ist im Dictionary enthalten")
if "Saigon" in d:
    print("Saigon ist in Dictionary enthalten")


for key in d:
    value = d[key]
    print(key)
    print(value)


print(d.items())

for k, v in d.items():
    print(k + " : " + v)


print("-----------------------------------")


my_dict1 = {i: i**2 for i in range(5)}
print(my_dict1)


my_dict2 ={i: i**2 if i > 3 else -(i**2) for i in range(5)}
print(my_dict2)

print("-----------------------------------")

my_dict3 = {'a': 1, 'b': 2}
my_dict4 = {'c': 3, 'd': 4}

#pre python 3.9
my_result = {**my_dict3, **my_dict4}
print(my_result)


#since python 3.9
my_result2 = my_dict3 | my_dict4
print(my_result2)