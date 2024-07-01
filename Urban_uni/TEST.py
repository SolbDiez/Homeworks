class Human:
    head = True
    _arms = True
    __legs = True

class Student(Human):
    pass

student = Student()
human = Human()


print(student._Human__legs)
