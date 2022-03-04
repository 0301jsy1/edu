#리스트
list_a=[1,2,3]
list_b=[4,5,6]
list_a.append(4) #추가
print(list_a) #[1, 2, 3, 4]
list_a.insert(1,5) #삽입
print(list_a) #[1, 5, 2, 3, 4]
list_a.extend(list_b) #병합 후 합집합
print(list_a) #[1, 5, 2, 3, 4, 4, 5, 6]
list_a.pop(3) #3번째 위치를 알려주고 삭제하시오. pop은 메서드
print(list_a) #[1, 5, 2, 4, 4, 5, 6] 
list_a.remove(5) #값을 알고 있는 경우 직접 삭제하지만 중복된 값이 있을 경우 첫번째 값을 삭제
print(list_a) #[1, 2, 4, 4, 5, 6]   
del list_a[0] #0번째 위치를 알려주고 삭제하시오. del은 키워드
print(list_a) #[2, 4, 4, 5, 6]
list_b.clear() #전체 삭제
print(list_b) #[]
#in/not in => true/false
print(3 in list_a)