class Student():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def name(self):
        return self.firstname + " " + self.lastname


class WorkingStudent(Student):
    def __init__(self, firstname, lastname, company):
        super().__init__(firstname, lastname)
        self.company = company

    def name(self):
        return super().name() + " " + self.company


w_student = WorkingStudent("Max", "Mustermann", "DDDD")
student = Student("Monika", "Mustermann")


print(type(w_student))
print(type(student))


print(isinstance(w_student, WorkingStudent))
print(isinstance(w_student, Student))

print(isinstance(student, WorkingStudent))
print(isinstance(student, Student))