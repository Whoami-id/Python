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


students = [
    WorkingStudent("Max", "Mustermann", "SDF"),
    Student("Monika", "Mustermann"),
    WorkingStudent("Erik", "Mustermann", "XXXXXX")
]

for s in students:
    print(s.name())


ss = WorkingStudent("gggggg", "Mustermann", "XXXXXX")
print(ss.firstname)