from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year =  year
        self.month = month
        self.day = day

    #instance methode
    def print_date(self):
        print("{0} {1} {2}".format(self.year, self.month, self.day))

    #class methode
    @classmethod
    def get_todays_date(cls):
        date = cls.__new__(cls)
        time = localtime()
        date.year = time.tm_year
        date.month = time.tm_mon
        date.day = time.tm_mday
        return date

    #static method
    @staticmethod
    def is_todays_date(year, month, day):
        time = localtime()
        if year == time.tm_year and month == time.tm_mon and day == time.tm_mday:
            return True
        else:
            return False


date1 = Date(2008, 10, 8)
date1.print_date()

data2 = Date.get_todays_date()
data2.print_date()

print(Date.is_todays_date(data2.year, data2.month, data2.day))