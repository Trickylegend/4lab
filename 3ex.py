import copy

class Faculty:
    name = ""
    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

class Student:
    name = ""
    date = 0

    math = 0
    eng = 0
    ec = 0
    oopip = 0

    def __init__(self, name, date):
        self.name = name
        self.date = date

    def get_name(self):
        return self.name

    def get_date(self):
        return self.date

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def get_math(self):
        return self.math

    def set_math(self, data):
        self.math = data

    def get_eng(self):
        return self.eng

    def set_eng(self, data):
        self.eng = data

    def get_ec(self):
        return self.ec

    def set_ec(self, data):
        self.ec = data

    def get_oopip(self):
        return self.oopip

    def set_oopip(self, data):
        self.oopip = data


st1 = Student("Vadim", 2000)
st2 = Student("Ilya", 1999)
st3 = Student("Ivan", 2001)

st2.set_eng(10)
st2.set_ec(7)
st2.set_oopip(9)
st2.set_math(10)

print("Оценки ", st2.get_name(), ": Экономика : ", st2.get_ec(), " Математика : ", st2.get_math(), " Англ: ", st2.get_eng())