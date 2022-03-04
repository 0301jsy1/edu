#pass 키워드 : 전체적인 골격 작성 없이 내부 연기
num=input("정수입력-> ")
num = int(num)

if num>0:
    pass
else:
    pass

if num>=0:
    if num==0:
        print('0')
    else:
        print('양수')
else:
    print('음수')

#반복문, 리스트(동적), 배열(정적)
array = [30, "abc", 3.14, True]
print(array)
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[-1])
print(array[1][-2]) #문자열만 인덱싱이 가능함

list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a[0])
print(list_a[1][2])
list_b = [[10,11]]
list_c = list_a + list_b
print(list_c)
list_d = list_c * 3
print(list_d)
list_a.append(4) #추가
print(list_a)
list_a.insert(0,10) #삽입
print(list_a)
list_a.extend(list_b) #확장
print(list_a)
print(list_b)
list_a.pop(2) #2번째 자리에서 빼낸다.
print(list_a)

del list_a[2] #2번째 자리를 삭제한다.
print(list_a)