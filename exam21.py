#객체지향언어 => 객체의 모음으로 프로그램 작성
#클래스 = 속성(명사 : 색, 수치, 재질) + 행위(기능, 함수)

class Student: #클래스 정의
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

students = [Student("Chosy",100,100,100),Student("park",10,90,30),Student("Cho",90,80,70),Student("sy",10,10,10)]  # Student() 클래스 생성자 함수