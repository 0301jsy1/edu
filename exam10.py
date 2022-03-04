#반복문, 조건문, 리스트, 딕셔너리, range
from os import remove


a = range(5)
print(a)
a = list(range(5))
print(a)
list_a=[0,1,2,3,4]
print(list_a)
a = list(range(0, 10, 1)) #숫자의 범위 0~10까지 1증감으로 출력하라
print(a)
b = list(range(1, 10, 2))
print(b)
c = list(range(2, 10, 3)) 
print(c)
d = list(range(3, 10, 4)) 
print(d)
for i in range(5): #0~4까지 반복하여 출력
    print(i,'의 반복 변수')
    print('{}의 반복 변수'.format(i))

for i in range(10,1,-2):
    print('{}의 반복 변수'.format(i))

array = [273, 32, 403, 57, 52]
for i in range(len(array)): #len(array) : 숫자의 길이 즉 갯수는 5개, range() : 범위, range(len(array)) : 5개 숫자의 범위 내에서 반복하라
    print('{}번째 데이터 : {}'.format(i, array[i]))

i=0
while i<10:
    print('{}번째 자료'.format(i))
    i+=1

list_c = [1,2,3,1,2,3,2]
value=2
while value in list_c:
    list_c.remove(value)

print(list_c)  

i=0
while True: #무한반복
    print("{}번째 반복 중...".format(i))
    i+=1
    #반복 종료
    input_msg = input("종료?(Y/N)")
    if input_msg in ["Y","y"]:
        break

list_a=[5,15,6,20,7,25]
print(list_a)  
#목록에서 10이상만 출력 
for i in list_a:
    if i<10:
        continue
    print(i)
    

list_a = [1,26,39,47,54]
print(list_a)
for i in list_a:
    if i<10:
        continue
    print(i)