#람다 => 함수(매개변수=함수,매개변수=값)
#내장함수=>map(함수,리스트),filter(함수,리스트)
#함수정의
def under_3(item):
    return item<3 #리턴된 값은 true가 됨

#리스트 정의
list_a=[1,2,3,4,5]

output_a=filter(under_3,list_a) #filter(조건식, 값)
print(list(output_a))

output_b=filter(lambda x:x<3,list_a) #lambda를 통해 간소화 (lambda 매개변수 : return 값, 매개변수)
print(list(output_b))

def power(item):
    return item*item #리턴된 값이 제곱근이며 true가 되어야 함

output_c=map(power,list_a)
print(list(output_c))

output_d=map(lambda x:x*x, list_a)
print(list(output_d))

output_e=[]
for i in list_a:
    output_e.append(i*i)
print(output_e)

#리스트내포
output_f=[i*i for i in list_a]
print(output_f)