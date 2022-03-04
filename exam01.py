print('hello')
print(1,2,3)
print("Chosy")
print(type('h'))
print(type(10))
print(type(10.5))
print(type(True))
print('"안녕"이라고 말했다.')
print("\"안녕\"이라고 말했다.")
print('"hello"\n"안녕"\n"Chosy"')
print('"hello"\t"안녕"\t"Chosy"')
print('동해물과 백두산이 마르고 닳도록\n하나님이 보우하사 우리나 라만세')
print("""동해물과 백두산이 마르고 닳도록 
하나님이 보우하사 우리나 라만세""")
print('''동해물과 
백두산이 
마르고 
닳도록 
하나님이 
보우하사 
우리나라
만세''')
print('''\
동해물과 
백두산이 
마르고 
닳도록 
하나님이 
보우하사 
우리나라
만세\
''')
print('''\
동해물과 
백두산이 
마르고 
닳도록 
하나님이 
보우하사 
우리나라
만세\
'''[1:10]) 
#슬라이싱
# [시작:끝] => 시작에서부터 끝-1 위치까지 추출하라 즉 인덱스 1~9번까지
print("hello"[1:3]) #1~2
print("hello"[:3]) #0~2
print('hello'[1:]) #1~
#Random.Range(1,4) => 1,2,3(정수일 때) : 최소값, 최대값-1