#함수, 변수, 상수 => 가독성 및 유지보수에 필요함
number_input=input("숫자 입력 : ")
radius=float(number_input) #자료형 변환시 -> float, int, str, list, dict
print(2*3.14*radius) #? 가독성 떨어짐 -> 원의 둘레 출력
print(3.14*radius*radius) #? 가독성 떨어짐 -> 원의 넓이 출력

#숫자 입력 함수
def number_input():
    output = input("숫자입력 : ")
    return float(output)

#원의 둘레 / 원의 넓이 출력 함수
def get_circumference(radius):
    return 2*3.14*radius

#출력 함수
def print_msg(msg):
    print("Output : ",msg)

radius=number_input()
msg = get_circumference(radius)
print_msg(msg)

#리스트[] / 딕셔너리{} / 튜플() -> 괄호 생략가능
list_a = [10,20,30]
dict_a = {1:1,2:2,3:3}
tuple_a = (10,20,30) #tuple_a = 10,20,30
print(list_a[0]) #인덱스
print(dict_a[3]) #키
print(tuple_a[0]) #인덱스
list_a[0] = 100
dict_a[1] = 100
#tuple_a[0] = 100 -> 튜플은 수정이 불가능, 입력된 값만 사용 가능
print(list_a[0]) #인덱스
print(dict_a[1]) #키
print(tuple_a[0]) #인덱스

a,b = 10,20
(c,d) = (30, 40)
print(a)
print(b)
print(c)
print(d)
#swap : 자리바꿈
a,b=b,a
c,d=d,c
print(a)
print(b)
print(c)
print(d)

#10은 0번째 자료입니다.
list_a = [10, 20, 30]
for i, value in enumerate(list_a): 
    print("{}은 {}번째 자료입니다".format(value,i))
#enumerate : “열거하다”의 뜻 
#enumerate() -> 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴

#목(//)과 나머지(%)
a,b=10,3
몫, 나머지 = divmod(a,b) #divmod() : 몫과 나머지 구하는 함수
print(몫)
print(나머지)

#기본자료형 => 문자, 숫자, bool
dict_a={(0,0):100, (0,1):200, (1,0):300, (1,1):400}
print(dict_a[0,0])

a = 10,3,5 #튜플
print(a[2])

#람다 : 매개변수로 함수를 받는다
def call_10_times(func):
    for i in range(10): #0~9
        func() #콜백함수

def print_hello():
    print('hello')

call_10_times(print_hello) #hello를 10번 출력하는 함수

def call_10_times(func,n):
    for i in range(n): #0~9
        func(i) #콜백함수

def print_hello(a):
    if a%2==0:
        print('짝수') #짝수
    else:
        print('홀수')

call_10_times(print_hello,3)
