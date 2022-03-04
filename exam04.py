#문자 검색
num = "hello".find("l") # 특정 문자나 문자열을 찾아주는 메서드
print(num)
num = "hello".rfind('l') #find()는 문자열을 찾을 때 왼쪽부터 시작하고, rfind()는 오른쪽 부터 시작
print(num)
#문자열 자르기
a = '10 20 30 40'.split(' ') #공백을 중심으로 숫자 자르기
print(a) #배열의 리스트 개념
#논리 연산자
print(True and True)
print(True or False) # True 둘다 False는 안됨
print(False or True) # True
print(not True) #부정
#if 조거문 / input => 문자 입력 / int => 문자를 정수로 변환
num = input('정수 입력 : ')
num = int(num)
if num>0:
    print("양수")
    print("입니다.")
if num<0:
    print("음수 입니다.")
else :
    print("0 입니다.")