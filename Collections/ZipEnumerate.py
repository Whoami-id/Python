my_list = [1,2,3,4,5]
my_tupble = (-1, -2, -3, -4)

zip_object = zip(my_list, my_tupble)

for v1, v2 in zip_object:
    print(v1 , v2)


for v3, v4 in zip(my_list, my_tupble):
    print(v3 + v4)

print("-------------------------------")

enum_object = enumerate(my_list)
for idx, val5, in enum_object:
    print(idx, val5)

print("-------------------------------")

for idx1, (val6, val7) in enumerate(zip(my_list, my_tupble)):
    print(idx1, val6, val7)