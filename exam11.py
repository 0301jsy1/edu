#리스트, 딕셔너리 반복문
numbers = [273, 103, 5, 32, 65, 9, 72]
#1. 100이상의 숫자만 출력
for number in numbers:
    if number >= 100:
        print('{}는 100이상의 숫자입니다.'.format(number))

#2. 273 홀수, 32은 짝수
for number in numbers:
    if number %2 == 0:
        print('{}는 짝수입니다.'.format(number))
    else:
        print('{}는 홀수입니다.'.format(number))

msg = ['짝수','홀수']
for number in numbers:
    print('{}는 {}입니다.'.format(number, msg[number%2]))

#3. 숫자의 자리 수 표현  / len(문자길이) -> 숫자길이X / str(숫자 -> 문자형) 
for number in numbers:
    print('{}는 {}자리 숫자입니다.'.format(number,len(str(number))))

#4. 이중 for문
list_of_list = [[1,2,3],[4,5,6,7],[8,9]]
for list in list_of_list:
    for i in list:
        print(i)

#5. 리스트 주가
list_a = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]
for i in list_a:
    output[(i-1)%3].append(i)
print(output)

#6. 딕셔너리('key':'value')
dict_a = {'name':'chosy'}
print(dict_a)
dict_a['name'] = 'chosylove'
dict_a['age'] = 20
print(dict_a)

dict_a=[{'name':'chosy','age':25},{'name':'chosylove','age':35},{'name':'chosylove1004','age':45}]
print(dict_a[0])
print(dict_a[0]['name'])

for person in dict_a:
    print('{}는 {}살 입니다.'.format(person['name'],person['age']))