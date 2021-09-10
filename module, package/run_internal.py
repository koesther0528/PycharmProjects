# import math
# print(math.ceil(3.5)) #천장
# print(math.floor(3.5)) #바닥
# print(round(3.5))
# print(round(3.4))
# print(math.pow(2, 10))
# print(math.sin(math.pi/2))
# # print(math.sin(math.pi))
#
# print('-'*20)
# import random
# print(random.random())
# print(random.randrange(1,10))
# print(random.randint(1,10))
# list1 = ['굶었음', '피자', '김치찜', '닭가슴살']
# print(random.choice(list1)) #list1중 하나
#
# print('before: ', list1)
# print(random.shuffle(list1)) #list1 섞기
# print('after: ', list1)
#
# print(random.sample(list1), 2) #list1에서 랜덤으로 n개 뽑기
#
# print('-'*20)
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.hour)
# birthday = datetime.datetime(2004, 5, 28)
# print(birthday)
# print(now - birthday)

#내 생일이 며칠 남았는지?
# import datetime
# today = datetime.date.today()
# mybirthday = datetime.date(2022,5,28)
# day = mybirthday - today
# print(day.days)

# #올해 크리스마스까지
# import datetime
# today = datetime.date.today()
# christmas = datetime.date(2021,12,25)
# day = christmas - today
# print(day.days)

#내가 태어난 날로부터 며칠이 지났는지
# import datetime
# today = datetime.date.today()
# mybirthday = datetime.date(2004,5,28)
# day = today - mybirthday
# print(day.days)

#로또 복권
# import  random
# lotto = random.sample(range(1,46), 6)
# print(lotto)

#중복되지않는 숫자 세자리
# import random
# num = list(range(1, 10))
# number = []
# for i in range(3):
#     number.append(num.pop(num.index(random.choice(num))))
# print(number)

#핸드폰요금
# import math
# bill = 62421
# print(bill//100*100)
# print((bill-bill%100))
# print(math.floor(bill/100)*100)

#평가계획
# import math
# print(round(93, -1))
# print(round(56, -1))

#마지막 번호 묻자
import random
last_number = input("마지막 번호는?")
#1~마지막 번호까지 숫자 리스트 만들자
list_class = list(range(1, int(last_number)+1))
#반복
while True:
    exclude_number = input("뺄 번호는?(enter 종료)")
    if exclude_number == '':
        break
#빼자
    list_class.remove(int(exclude_number))
    print(list_class)
#다 뺐으면 반복 끝내자
#섞자
random.shuffle(list_class)
print('자리\t학생번호')
for i, number in enumerate(list_class):
    print(f'{i+1}\t{number}')
