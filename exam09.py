#반복문, 리스트 : []
list_a = [1,2,3]
for i in list_a: # C#의 foreach in과 같다.
    print(i)

for i in "hello": #문자열의 경우 인덱싱이 가능
    print(i)

#반복문, 딕셔너리 : {}
dict_a = {'name':'chosy','age':20} #{ key : value, key : Value}
print(dict_a['name'])
print(dict_a['age']) #dict_a[key]
dict_a['age'] = 23 #자료 수정, 기존의 key 수정
print(dict_a['age'])
dict_a['tel'] = '010-6609-2994' #자료 추가, 기존의 key 추가
print(dict_a)
del dict_a['age'] #자료 삭제, 기존의 key 삭제
print(dict_a)
#자료 검색, 기존의 key 검색
key = input("키 입력 : ")
if key in dict_a:
    print(dict_a[key])
else:
    print('없음')

value = dict_a.get('tel') 
print(value)

value = dict_a.get('address')
if value == None:
    print('없음')
else:
    print(value)

for key in dict_a:
    print(key, ':', dict_a[key])

for num in dict_a:
    print(num)