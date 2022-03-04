#짝수 : 0,2,4,6,8 / 홀수 : 1, 3, 5, 7, 9 => 구분
num = input('정수 입력 : ')
last_num = int(num[-1])
print(last_num)

# last_num == 0 -> 관계 연산자 즉 last_num이 0과 같니? / last_num = 0 -> 대입 연산자 즉 last_num이 0 이니?
if last_num==0 or last_num==2 or last_num==4\
    or last_num==6 or last_num==8:
    print("짝수 입니다.")
else :
    print("홀수 입니다.")

num1 = input('정수 입력 : ')
last_num1 = int(num1)
print(last_num1)

if last_num1%2==0:
    print("짝수")
else :
    print("홀수")

#성적처리
num2 = input('정수 입력 : ')
last_num2 = float(num2)
print(last_num2)

if last_num2==100:
    print("A+")
elif last_num2>=90:
    print("A")
elif last_num2>=80:
    print("B")
elif last_num2>=70:
    print("C")
else:
    print("F")