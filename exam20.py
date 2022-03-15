#제네레이터 => 이터레이터를 직접 만들때 사용하는 코드
#yield 양보한다 -> 흐름을 제어함

def test():
    print("함수를 호출")
    yield "hello" #제네레이터 함수로 정의한 것

print("A 지점 통과") # A 지점 통과
next(test()) # 함수를 호출
print(next(test())) # 함수를 호출, hello
   
def test1():
    print("A 지점 통과")
    yield 1  #양보한다, 흐름이 바뀐다.
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
    yield 3

print("D 지점 통과") #D 지점 통과
print(next(test1())) #A 지점 통과, 1
print("E 지점 통과") #E 지점 통과
print(next(test1())) #A 지점 통과, 1
print("F 지점 통과") #F 지점 통과
print(next(test1())) #A 지점 통과, 1

output = test1()
print("D 지점 통과") #D 지점 통과
a=print(next(output))
print(a) #A 지점 통과, 1, none
print("E 지점 통과") #E 지점 통과
b=print(next(output)) 
print(b) #B 지점 통과, 2, none
print("F 지점 통과")  #F 지점 통과
c=print(next(output))
print(c) #C 지점 통과, 3, none

output=test1()
print("D 지점 통과")  #D 지점 통과
a=next(output)
print(a)
print("E 지점 통과")
b=next(output)
print(b)
print("F 지점 통과")
c=next(output)
print(c)