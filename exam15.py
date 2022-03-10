#피보나치수열 = 재귀함수 = 메모화 -> 1+1+2+3+5+8+13... => n번째항 = (n-2)번째항 + (n-1)번째항
count=0
def fibo(n):
    global count
    count+=1
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
print(fibo(8))
print(count)
#fibo(4)=fibo(3)+fibo(2)
#fibo(4)=fibo(2)+fibo(1)+1
#fibo(4)=1+1+1

#7=(6+5)                      +(5+4)            +(4+3)      +(3+2)  +(2+1)+(1+0)+(0-1)
#7=(1+1+1+1+1+1+1+1+1+1+1+1+1)+(1+1+1+1+1+1+1+1)+(1+1+1+1+1)+(1+1+1)+(1+1)+(1)  +(1)
#8=(7+6)                                      +(6+5)                      +(5+4)            +(4+3)      +(3+2)  +(2+1)+(1+0)+(0-1)
#8=(1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1)+(1+1+1+1+1+1+1+1+1+1+1+1+1)+(1+1+1+1+1+1+1+1)+(1+1+1+1+1)+(1+1+1)+(1+1)+(1)  +(1)

dict_a={1:1,2:1}
count=0
def fibo(n):
    global count
    count+=1
    if n in dict_a: #{1,2} key의 집합
        return dict_a[n]
    else:
        output=fibo(n-1)+fibo(n-2)
        dict_a[n]=output
        return output
print(fibo(100))
print(count)
#fibo(4)=fibo(3)+fibo(2)
#fibo(4)=fibo(2)+fibo(1)+1
#fibo(4)=1+1+1