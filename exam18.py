#파일처리 -> 외부에 있는 다른 대상과의 소통
#1. 어떤 대상?? 텍스트파일(텍스트에디터 = 메모장)
#바이너리파일(0,1) -> 이미지, 동영상, 엑셀
#2. 어떻게?? 쓰기/읽기

file = open('test.txt','w') #파일이 없으니  쓰기(write) 모드로 열어라
file.write("hello")
file.close()

file = open('test.txt','a') #글자 추가(append) 모드로 열어라
file.write("chosy")
file.close()

file = open('test.txt','r') #글자 읽기(read) 모드로 열어라
print(file.read())
file.close()

with open('test.txt','r') as file: #file.close() 생략가능
print(file.read())