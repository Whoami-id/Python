student = ["Max", "Monika", "Erik", "Franziska"]

last_student = student.pop()
print(last_student)
print(student)

student = ["Max", "Monika", "Erik", "Franziska"] + ["ASDF"]
print(student)

del student[3]
print(student)

student.remove("Monika")
print(student)