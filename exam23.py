#클래스 -> 객체(속성+행위)를 생성하는 구조도
class Student:
    count = 0 # 클래스의 변수
    students=[]
    #생성자
    def __init__(self,name,age):
        self.name=name # 인스턴스 변수
        self.age=age

        Student.count += 1 # 클래스 변수를 증가
    
    @classmethod # 클래스의 메소드 선언
    def print(cls):
        print('---학생목록---')
        for studentss in cls.students:
            print('학생이당')

    #함수(관계 비교 연산자 : ==, !=, >, <, >=, <=)
    def __eq__(self, other):
        print("eq함수") # ==
        return self.age == other.age
    def __ne__(self, other):
        print("ne함수") # !=
        return self.age != other.age
    def __gt__(self, other): # >
        print("gt함수")
        return self.age > other.age
    def __ge__(self, other): # >=
        print("ge함수")
        return self.age >= other.age


student=[
    Student('Chosy',29),
    Student('Chosy',19)
    ]

print(student[0].age==student[1].age) #eq함수 => False
print(student[0].name==student[1].name) #True
print(student[0].name>student[1].name) #false
print(student[0].age>student[1].age) #gt함수 => True
print(student[0]==student[1]) # => eq함수, false
print(student[0]>student[1]) # => gt함수, True
print(student[0]>=student[1]) # ge함수, True
print(student[0]<=student[1]) # ge함수, False
print(Student.count)
Student.print()