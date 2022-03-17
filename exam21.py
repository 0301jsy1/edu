#객체지향언어 => 객체의 모음으로 프로그램 작성
#클래스 = 속성(명사 : 색, 수치, 재질) + 행위(기능, 함수)

class Student: #클래스 정의
    def __init__(self, name, kor, eng, mat): #def : 함수, __init__ : 생성자 정의, __del__ : 삭제자 정의
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        print("--생성자 호출--")

    def get_sum(self): #합계 구하는 함수
        return self.kor + self.eng + self.mat
    
    def get_avg(self): #평균 구하는 함수 : 평균 = 합계/개수
        return self.get_sum()/3

    def to_string(self): #문자를 시각화하는 함수
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_avg())

students = [
    Student("Chosy",100,100,100),
    Student("park",10,90,30),
    Student("Cho",90,80,70),
    Student("sy",10,10,10)
    ]  # Student() 클래스 생성자 함수

print("이름","합계","평균",sep="\t")
for student in students:
    print(student.to_string())