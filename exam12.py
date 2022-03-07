#name : 기사
#level : 12
#sword : 칼
#armor : 플레이트
#skill : 베기
#skill : 세게 베기
#skill : 아주 세게 베기

#리스트, 딕셔너리<-->반복문
#문자,숫자 
#딕셔너리 type() is dict =>true/false
#리스트   type() is list =>true/false
#character[key][items_key]=>value

character={
    "name":"기사",
    "level":12,
    "items":{"sword":"칼","armor":"플레이트"},
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        #character[key]={"sword":"칼","armor":"플레이트"}
        for items_key in character[key]:
            print("{} : {}".format(items_key,character[key][items_key]))
        pass
    elif type(character[key]) is list:
        #skill(key) : 베기(value)
        #character[key]=["베기","세게 베기","아주 세게 베기"]
        for value in character[key]:
            print("{} : {}".format(key,value))
        pass
    else:
        print("{} : {}".format(key,character[key]))