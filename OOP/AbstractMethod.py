import abc



class Base(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def m1(self):
        return

    @staticmethod
    @abc.abstractmethod
    def m2(self):
        return

    @classmethod
    @abc.abstractmethod
    def m3(cls):
        return


class MyClass(Base):
    def m1(self):
        return "ma1"

    def m2(self):
        return "m2"

    def m3(cls):
        return "m3"