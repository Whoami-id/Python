class Student():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.term = 1

    def get_name(self):
        print(self.first_name + " " + self.last_name + " semester: " + str(self.term))

    def increase_term(self):
        self.term = self.term + 1


erik = Student("Erik", "Mustermann")
print(erik.first_name)
erik.get_name()
erik.increase_term()
erik.get_name()
