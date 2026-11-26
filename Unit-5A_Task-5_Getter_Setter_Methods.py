class Student:
    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, value):
        if 0 <= value <= 100:
            self.__marks = value
        else:
            print("Invalid marks")

s = Student()
s.set_marks(85)
print("Marks:", s.get_marks())
s.set_marks(150)  