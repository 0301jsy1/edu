class Student:
    def __init__(self, name):
        self.name = name
    
    def study(self):
        print("학생은 공부합니다.")

    def __str__(self):
        return "나의 이름은 {}입니다.".format(self.name)


class Teacher:
    def teach(self):
        print("선생은 가르칩니다.")

classRoom = [Student("chosy"),Student("sinmn"),Teacher(),Student("kimsh")]

for person in classRoom:
    if isinstance(person,Student):
        person.study()
        print(str(person))
    elif isinstance(person,Teacher):
        person.teach()