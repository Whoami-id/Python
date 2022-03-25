t = (1, 2, 3)
print(t)

student = ("Max Müller", 22, "Informatik")
name = student[0]
age = student[1]
subject = student[2]

n, a, s = student
print(n)
print(a)
print(s)



def get_student():
    return "Max Müller", 22, "Informatik"


name1, age1, subject1 = get_student()
name4, *packed_tuple = get_student()
print(name4)
print(packed_tuple)


s = [
    ("Max", 22),
    ("Monika", 23)
]

for name2, age2 in s:
    print(name2)
    print(age2)
