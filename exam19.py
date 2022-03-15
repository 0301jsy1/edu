import random

한글 = list('가나다라마바사아자차카타파하')

with open('info.txt','w') as file:
    for i in range(20):
        name = random.choice(한글) + random.choice(한글)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        file.write('{},{},{}\n'.format(name,weight,height))

with open('info.txt','r') as file:
    for line in file:
        (name,weight,height) = line.strip().split(',') #쉼표를 가지고 구분해서 튜플(name.weight,height)에 담아라
        print(file.read())