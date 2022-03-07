#기본함수
#리스트 관련 함수(function)
numbers = [103, 52, 273, 32, 77]
print(min(numbers)) 
print(max(numbers))
print(sum(numbers))
list_reversed = reversed(numbers) #numbers 리스트의 숫자들을 역순으로 표현하는 메소드(class)
print(list(list_reversed)) #list형으로 형변환 필요
for i in list_reversed:
    print(i)

#0번째 자리 출력 메소드 즉 0번째~2번째 : range, 길이(갯수)를 재라 즉 3개 : len 
list_a = ['요소A','요소B','요소C']
for i in range(len(list_a)):
    print('{}번째 요소는 {}이다.'.format(i, list_a[i]))

#열거형 함수 사용하기 : enumerator() => 자리와 요소 값을 출력하는 함수
print(list(enumerate(list_a))) #list형으로 형변환 필요
for i, value in enumerate(list_a): #enumerator() 함수 사용시 2개 인수(i, value) 필요함
    print('{}번째 요소는 {}이다.'.format(i, value))

#items() 함수
dict_a = {'key1':'value1', 'key2':'value2'}
for key in dict_a:
    print(key, ":", dict_a[key])
print(list(dict_a.items()))
for key, value in dict_a.items():
    print(key, ":", value)

#리스트 내포 => [표현식 for문]
array=[]
#0,2,4,6,8,10,.... => 0,4,16,36,64,100,...
for i in range(0,20,2):
    array.append(i*i)
    if i*i>=100: #글자수가 3자리 이상만
        array.append(i*i)
print(array)

array_a=[i*i for i in range(0,20,2) if i*i>=100]
print(array_a)
