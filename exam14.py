#구문 내부에 여러 줄
number = int(input('정수 입력 : '))
if number%2==0:
    print(
"""'입력한 문자열은 {}입니다. 
 {}은 짝수이다.'""".format(number,number)
 )
    pass
else:
    pass

print("::".join(["a","b","c"]))
print('\n'.join(["a","b","c"]))

#함수, 모듈, 클래스
def print_n_times(n,value): #매개 변수는 2개
    for i in range(n): #0~4
        print(value)
print_n_times(5,'hello')
print_n_times(3,'chosy')
print_n_times(2,'안녕')

def print_n_times(n,*values): #매개 변수는 2개(일반 매개 변수, 가변 매개변수), 맨뒤는 가변 매개변수, 기본 매개변수로 끝
    for i in range(n): #0~2
        #print(values)
        for value in values:
            print(value)
print_n_times(3,'hello','안녕','chosy')

def print_n_times(*values,n=2): #매개 변수는 2개(가변 매개 변수, 기본 매개변수)
    for i in range(n): #0~2
        #print(values)
        for value in values:
            print(value)
print_n_times('hello','안녕','chosy',3) #가변 매개 변수

def print_n_times(*values,n=2): #매개 변수는 2개(가변 매개 변수, 기본 매개변수)
    for i in range(n): #0~2
        #print(values)
        for value in values:
            print(value)
print_n_times('hello','안녕','chosy',n=3) #가변 매개 변수, 키워드 기본 매개변수 추가

def print_n_times(i, *values,n=2): #매개 변수는 3개(일반 매개 변수, 가변 매개 변수, 기본 매개변수)
    for i in range(n): #0~2
        #print(values)
        for value in values:
            print(value)
print_n_times(10, 'hello','안녕','chosy',n=3) #일반 매개 변수, 가변 매개 변수, 키워드 기본 매개변수 추가

def test(a, b, c):
    print(a+b+c)
test(2,3,4)

def test(a, b, c=100):
    print(a+b+c)
test(2,3)

def test(a, b=100, c=100):
    print(a+b+c)
test(2)

def test(a, b=100, c=100):
    print(a+b+c)
test(2,10,10)

def test(a, b=100, c=100):
    print(a+b+c)
test(2,b=10,c=10)

def test(a, b=100, c=100):
    return a+b+c
value = test(2,10,10)
print(value)

def sum_all(start,end):
    output = 0
    for i in range(start,end+1):
        output += i
    return output
value = sum_all(1,100)
print("합계 : ", value)