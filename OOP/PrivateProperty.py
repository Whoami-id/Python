class Student():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__term = 1

    def get_name(self):
        print(self.first_name + " " + self.last_name + " semester: " + str(self.__term))

    def increase_term(self):
        if self.__term >= 9:
            return
        self.__term = self.__term + 1

    def get_term(self):
        return self.__term




class User:
    def __init__(self,name, id):
        self.name = name
        self._id = id

    def __str__(self):
        return "{}{}".format(self.name, self._id)


    #Getter for id
    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, new_id):
        self.id = new_id


u1 = User("jan", 23)
u1.name = "peter"
print(u1.name)


erik = Student("Erik", "Mustermann")
print(erik.first_name)

erik.get_name()
erik.increase_term()
erik.get_name()
print(erik.get_term())








