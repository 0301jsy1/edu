#input('인사말을 입력 : ') #입력
num = input("숫자입력 : ") #무엇을 입력하든 문자
#type(num) #class str => 자료형은 문자
#type(int(num)) #순간적 형변환
int_num = int(num)
print(int_num+20)
str_num = str(num)
str_numch = str_num+'ch'
print(str_numch)
name = input("이름 : ")
print(name)
#format() 서식지정 : 데이터 시각화 ... "주어".format(목적어)
str_num = "{}년 {}월 {}일 {}요일".format(2022,2,24,"목") # (10이라는 숫자를) {문자로} 변형해서 변수에 저장
print(type(str_num))
print(str_num)
int_a = '{:+d}'.format(52) # :d : 정수라고 표기
print(int_a) #+52
int_b = '{:+5d}'.format(52)
print(int_b) #  +52
int_c = '{:=+5d}'.format(52)
print(int_c) #+  52
int_d ='{:+04d}'.format(52)
print(int_d) #+052
int_e = '{:=+05d}'.format(52)
print(int_e) #+0052
int_f = '{:+f}'.format(52.32) # :d : 정수라고 표기
print(int_f) #+52
int_g = '{:+5f}'.format(52.32)
print(int_g) #  +52
int_h = '{:=+5f}'.format(52.32)
print(int_h) #+  52
int_i ='{:+04f}'.format(52.32)
print(int_i) #+052
int_j = '{:=+05f}'.format(52.32)
print(int_j) #+0052