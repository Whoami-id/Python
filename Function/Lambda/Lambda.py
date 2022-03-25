#KEYWORD, Params (tuple): expression (without return keyword)


students = [
    ("Max",3),
    ("Monika", 2),
    ("Erik", 1),
    ("Franziska", 4)
]

def students_key(student):
    print(student[1])
    return student[1]

students.sort(key=students_key)
print(students)


students.sort(key=lambda student: student[1])
print(students)

print("-----------------------------------------")


my_dict = {"jan": [26, 84], "peter": [100, 0], "dennis": [22, 70]}
print(sorted(my_dict.items(), key= lambda x: x[0], reverse= False))
print(sorted(my_dict.items(), key= lambda x: x[1][1], reverse= False))

print("----------------------------------")

my_list = [[12,34], [-1,4], [5,3]]
my_list.sort(key=lambda x: x[0])
print(my_list)
