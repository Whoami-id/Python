xs = [1,2,3,4,5,6,7,8]
ys = [x * x for x in xs]
print(ys)

students = ["Max", "Monika", "Erik", "Franziska"]
l = [len(student) for student in students ]
print(l)



list2 = [(i**2 if i <= 2 else (-1 if i == 1 else i)) for i in range(5)]
print(list2)



list3 = [0 for _ in range(5)]
print(list3)


list4 = [i for i in range(5) if i < 3]
print(list4)



