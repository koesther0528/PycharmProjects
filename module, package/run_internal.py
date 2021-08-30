import math
print(math.ceil(3.5)) #천장
print(math.floor(3.5)) #바닥
print(round(3.5))
print(round(3.4))
print(math.pow(2, 10))
print(math.sin(math.pi/2))
# print(math.sin(math.pi))

print('-'*20)
import random
print(random.random())
print(random.randrange(1,10))
print(random.randint(1,10))
list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
print(random.choice(list1)) #list1중 하나

print('before: ', list1)
print(random.shuffle(list1)) #list1 섞기
print('after: ', list1)

print(random.sample(list1), 2) #list1에서 랜덤으로 n개 뽑기

print('-'*20)
import datetime
now = datetime.datetime.now()
print(now)
print(now.day)
print(now.hour)
birthday = datetime.datetime(2004, 5, 28)
print(birthday)
print(now - birthday)