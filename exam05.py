import datetime

now = datetime.datetime.now()
print(now.year,'년')
print(now.month,'월')
print(now.day,'일')
print('{}년 {}월 {}일'.format(now.year, now.month, now.day))

if now.hour<12:
    print('현재 시간은 {}시 이므로 오전 입니다.'.format(now.hour))
if now.hour>12:
    print('현재 시간은 {}시 이므로 오후 입니다.'.format(now.hour))

if now.month>=3 and now.month<=5:
    print('현재 {}월 이므로 봄입니다.'.format(now.month))
if now.month>=6 and now.month<=8:
    print('현재 {}월 이므로 여름입니다.'.format(now.month))
if now.month>=9 and now.month<=11:
    print('현재 {}월 이므로 가을입니다.'.format(now.month))    
if now.month<=12 and now.month<=2:
    print('현재 {}월 이므로 겨울입니다.'.format(now.month))