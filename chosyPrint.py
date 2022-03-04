msg = '   ab cde  '
msg1 = msg.upper() #대문자로 만들어라
msg2 = msg1.lower() #소문자로 만들어라
msg3 = msg2.strip() #앞뒤 쓸데없는 공백 없애기
msg4 = msg2.lstrip() #왼쪽 쓸데없는 공백 없애기
msg5 = msg2.rstrip() #오른쪽 쓸데없는 공백 없애기
msg6 = msg.isalpha() #String이 Alphabet인지 확인해주는 함수
msg7 = msg.isupper() #대소문자 판별하는 함수
print(msg)
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print(msg6)
print(msg7)