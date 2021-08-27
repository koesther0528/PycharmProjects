#숫자 자료형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

#문자열 자료형
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

#boolean 자료형
# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))

#변수
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# in_abult = age >=3
#
# print("우리집" + animal + "의 이름은" + name + "예요")
# hobby = "공놀이"
# print(name, "는" , age, "살이며", hobby, "을 아주 좋아해요")
# print(name, "는 어른일까요?", str(in_abult))

#퀴즈
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

#연산자
# print(1 != 3)
# print(not(1!=3))
#
# print((3>0) and (3<5))
# print((3>0) & (3<5))
#
# print((3>0) or (3>5))
# print((3>0) | (3>5))
#
# print(5>4>3)
# print(5>4>7)

#간단한 수식
# print(2 + 3 *4)
# print((2+3)*4)
# number = 2+3*4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# print(number)
# number -= 2
# print(number)
#
# number %= 2
# print(number )

#숫자처리함수
# print(abs(-5))
# print(pow(4,2))
# print(max(5,12))
# print(min(5,12))
# print(round(3.14))
# print(round(4.99))
#
# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

#랜덤함수
# from random import *

# print(random())
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 10) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)
# print(int(random() * 45) + 1)

# print(randint(1, 45))

#퀴즈2
# from  random import *
#
# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정")

#문자열
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """나는 소년이고, 파이썬은 쉬워요"""
# print(sentence3)

#슬라이싱
# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0~2직전
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])
# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) " + jumin[-7:])

#문자열처리함수
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("python", "java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index +1)
# print(index)

# print(python.find("Java"))
# print(python.index("Java"))
# print("hi")

# print(python.count("n"))

#문자열포멧
# print("a" + "b")
# print("a" + "b")
#
# print("나는 %d살입니다." %20)
# print("나는 %s을 좋아해요." % "파이썬")
# print("Apple은 %c로 시작해요" % "A")
#
# print("나는 %s살입니다." %20)
# print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))
#
# print("나는 {}살입니다." .format(20))
# print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))
#
# print("나는 {age}살이며, {color}색을 좋아해요" .format(age=20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요" .format(color="빨간", age=20))
#
# age = 20
# color = '빨간'
# print(f"나는 {age}살이며, {color}색을 좋아해요")

#탈출문자
# print("백문이 불여일견\n 백견이 불여일타")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")
#
# print("Red Apple\rPine")
#
# print("Redd\bApple")
#
# print("Red\tApple")

#퀴즈3
# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다." .format(url, password))

#리스트
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)
#
# subway = ["유재석" , "조세호", "박명수"]
# print(subway)
#
# print(subway.index("조세호"))
# subway.append("하하")
# print(subway)
#
# subway.insert(1, "정형돈")
# print(subway)
#
# print(subway.pop())
# print(subway)
#
# # print(subway.pop())
# # print(subway)
#
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)
#
# num_list.reverse()
# print(num_list)
#
# num_list.clear()
# print(num_list)
#
# mix_list = ["조세호" , 20 , True]
# print(mix_list)
#
# num_list.extend(mix_list)
# print(num_list)

#사전
# cebinet = {3:"유재석" , 100:"김태호"}
# # print(cebinet[3])
# # print(cebinet[100])
# #
# # print(cebinet.get(3))
# # print(cebinet.get(5, "사용가능"))
# # print("hi")
#
# # print(3 in cebinet)
# # print(5 in cebinet)
#
# cebinet = {"A-3" : "유재석", "B-100" : "김태호"}
# print(cebinet["A-3"])
# print(cebinet["B-100"])
#
# print(cebinet)
# cebinet["A-3"] = "김종국"
# cebinet["B-100"] = "조세호"
# print(cebinet)
#
# del cebinet["A-3"]
# print(cebinet)
#
# print(cebinet.keys())
#
# print(cebinet.values())
#
# print(cebinet.items())
#
# print(cebinet.clear())
# print(cebinet)

#튜플
# menu = ("돈까스" , "치즈까스")
# print(menu[0])
# print(menu[1])
#
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
#
# (name, age, hobby) = ("김종국" , 20, "코딩")
# print(name,age,hobby)

#세트
# my_set = {1,2,3,3,3}
# print(my_set)
#
# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석," , "박명수"])
#
# print(java&python)
# print(java.intersection(python))
#
# print(java | python)
# print(java.union(python))
#
# python.add("김태호")
# print(python)
#
# java.remove("김태호")
# print(java)

#자료구조의 변경
# menu = {"커피", "우유" , "주스"}
# print(menu, type(menu))
#
# menu = list(menu)
# print(menu, type(menu))
#
# menu = tuple(menu)
# print(menu, type(menu))
#
# menu = set(menu)
# print(menu, type(menu))

#퀴즈4
# from random import *
# users = range(1,21)
# # print(type(users))
# users = list(users)
# # print(type(users))
#
# print(users)
# shuffle(users)
# print(users)
#
# winners = sample(users, 4)
#
# print(" --당첨자 발표--")
# print("치킨 당첨자 : {0}" .format(winners[0]))
# print("커피 당첨자 : {0}" .format(winners[1:]))
# print("--축하합니다--")

#if
# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp <10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지마세요")

#for
# print("대기번호 1")
# print("대기번호 2")
# print("대기번호 3")
# print("대기번호 4")

# for waiting_no in range(1,6):
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다".format(customer))

#while
# customer = "토르"
# index = 5
# while index >=1:
#     print("{0}, 커피가 준비 되었습니다.{1}번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.호출 {1} 회".format(customer,index))
#     index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")

#continue&break
# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지.{0}는 교무실로 따라와".format(student))
#         break
#     print("{0},책을 읽어봐".format(student))

#한줄for
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)
#
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)
#
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

#퀴즈5
# from random import *
# cnt = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
#         cnt += 1
#     else:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i,time))
# print("총 탑승 승객: {0}분".format(cnt))

#함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
#
# open_account()

#전달값과 반환값
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")
# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance+money))
#     return balance + money
# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
#         return balance
# def withdraw_night(balance,money):
#     commission = 100
#     return  commission, balance - money - commission
#
# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
# print(balance)
# commission, balance = withdraw_night(balance,500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다".format(commission, balance))

#기본값
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t나이: {1}\t주 사용언어: {2}".format(name, age,main_lang))
# profile("유재석")
# profile("김태호")

#키워드값
# def profile(name,age,main_leng):
#     print(name,age,main_leng)
#
# profile(name="유재석", main_leng="파이썬", age=20)
# profile(main_leng="자바", age=25, name="김태호")

#가변 인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1{\t".format(name,age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
#
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Javascript")
# profile("김태호", 25, "Kotlin", "Swift")

#지역변수, 전역변수
# gun = 10
# def checkpoint(soldiers):
#     global gun
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun
#
#
# print("전체 총: {0}".format(gun))
# gun = checkpoint_ret(gun,2)
# print("남은 총: {0}".format(gun))

#퀴즈6
# def std_weight(height, gender):
#     if gender == "남자":
#         return height*height*22
#     else:
#         return height*height*21
#
# height = 175
# gender = "남자"
# weight = round(std_weight(height / 100, gender),2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

#클래스
#마린: 공격유닛, 군인, 총을 쏠수 있음
# name = "마린" #유닛의 이름
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력
#
# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp, damage))
#
# #탱크: 공격 유닛, 탱크, 포, 일반모드/ 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력{1}\n".format(tank_hp, tank_damage))
#
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
#
# print("{0} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력{1}\n".format(tank2_hp, tank2_damage))
#
# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))
#
# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# class Unit:
#     def __init__(self,name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

#__init__
# class Unit:
#     def __init__(self,name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#
# marine1 = Unit("마린",40,5)
# marine2 = Unit("마린",40,5)
# tank = Unit("탱크",150,35)

#멤버 변수
# class Unit:
#     def __init__(self,name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#
# # marine1 = Unit("마린",40,5)
# # marine2 = Unit("마린",40,5)
# # tank = Unit("탱크",150,35)
#
# #레이스: 공중유닛, 비행기, 클로킹
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage))
#
# #마인드 컨트롤: 상대방 유닛을 내 것으로 만드는것
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.cloking = True
#
# if wraith1.cloking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

#메소드
# class Unit:
#     def __init__(self,name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력{1}".format(self.hp, self.damage))
#공격유닛
# class AttackUnit:
#     def __init__(self,name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : {1} 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))
# #파이어뱃: 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

#상속
# class Unit:
#     def __init__(self,name, hp):
#         self.name = name
#         self.hp = hp
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : {1} 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))
# #메딕: 의무병
#
#
# #파이어뱃: 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16)
# firebat1.attack("5시")
#
# firebat1.damaged(25)
# firebat1.damaged(25)

#다중 상속
# class Unit:
#     def __init__(self,name, hp):
#         self.name = name
#         self.hp = hp
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp, damage):
#         Unit.__init__(self,name,hp)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : {1} 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))
#
# #드랍쉽: 공중유닛, 수송기.마린 / 파이어뱃/ 탱크등을 수송. 공격X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#         def __init__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp, damage)
#             Flyable.__init__(self,flying_speed)
# #발키리
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

#메소드 오버라이딩
# class Unit:
#     def __init__(self,name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp,speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : {1} 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))
#
# #드랍쉽: 공중유닛, 수송기.마린 / 파이어뱃/ 탱크등을 수송. 공격X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#         def __init__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp,0, damage)
#             Flyable.__init__(self,flying_speed)
#         def move(self, location):
#             print("[공중 유닛 이동]")
#             self.fly(self.name, location)
# #벌처: 지상유닛, 기동성 좋음
# vulture = AttackUnit("벌쳐",80,10,20)
#
# #배틀크루저:공중유닛, 체력도 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)
#
# vulture.move("11시")
# battlecruiser.move("9시")

#pass
# class Unit:
#     def __init__(self,name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp,speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : {1} 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))
#
# #드랍쉽: 공중유닛, 수송기.마린 / 파이어뱃/ 탱크등을 수송. 공격X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#         def __init__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp,0, damage)
#             Flyable.__init__(self,flying_speed)
#         def move(self, location):
#             print("[공중 유닛 이동]")
#             self.fly(self.name, location)
# #건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass
#
# supply_depot = BuildingUnit("서폴라이 디폿", 500, "7시")
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")
#
# def game_over():
#     pass
#
# game_start()
# game_over()

#super
# class Unit:
#     def __init__(self,name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp,speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name,damage))
#         self.hp -= damage
#         print("{0} : {1} 현재 체력은 {1} 입니다".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다".format(self.name))
#
# #드랍쉽: 공중유닛, 수송기.마린 / 파이어뱃/ 탱크등을 수송. 공격X
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#         def __init__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp,0, damage)
#             Flyable.__init__(self,flying_speed)
#         def move(self, location):
#             print("[공중 유닛 이동]")
#             self.fly(self.name, location)
# #건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self,name,hp, 0)
#         super().__init__(name,hp, 0)
#         self.location = location

#스타크래프트 전반전
# class Unit:
#     def __init__(self,name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))
#
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp,speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40,1,5)
#
#     #스팀팩: 일정시간동안 이동,공격,속도 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다 (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#
# class Tank(AttackUnit):
#     #시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 기능
#     seize_develped = False
#
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150,1,35)
#         self.seize_mode = False
#
#     def set_seize_mode(self):
#         if Tank.seize_develped == False:
#             return
#         #현재 시즈모드가 아닐때
#         if self.seize_mode(self):
#             if Tank.seize_mode == False:
#                 print("{0} : 시즈모드로 전환".format(self.name))
#                 self.damage *= 2
#                 self.seize_mode = True
#             else:
#                 print("{0} : 시즈모드 해제".format(self.name))
#                 self.damage /= 2
#                 self.seize_mode = False
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#         def __init__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp,0, damage)
#             Flyable.__init__(self,flying_speed)
#         def move(self, location):
#             print("[공중 유닛 이동]")
#             self.fly(self.name, location)
#
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False
#
#     def clocking(self):
#         if self.clocked == True:
#             print("{0}  클로킹 모드 해제".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정".format(self.name))
#             self.clocked = True

#스타크래프트 후반전
# from random import *
#
# class Unit:
#     def __init__(self,name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다".format(name))
#
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
#
# #공격유닛
# class AttackUnit(Unit):
#     def __init__(self,name, hp,speed, damage):
#         Unit.__init__(self,name,hp, speed)
#         self.damage = damage
#
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 [공격력 {2}]".format(self.name, location, self.damage))
#
# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40,1,5)
#
#     #스팀팩: 일정시간동안 이동,공격,속도 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다 (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))
#
# class Tank(AttackUnit):
#     #시즈모드: 탱크를 지상에 고정시켜, 더 높은 파워로 공격 기능
#     seize_develped = False
#
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150,1,35)
#         self.seize_mode = False
#
#     def set_seize_mode(self):
#         if Tank.seize_develped == False:
#             return
#         #현재 시즈모드가 아닐때
#             if self.seize_mode == False:
#                 print("{0} : 시즈모드로 전환".format(self.name))
#                 self.damage *= 2
#                 self.seize_mode = True
#             else:
#                 print("{0} : 시즈모드 해제".format(self.name))
#                 self.damage /= 2
#                 self.seize_mode = False
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name,location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
#
# class FlyableAttackUnit(AttackUnit, Flyable):
#         def __init__(self, name, hp, damage, flying_speed):
#             AttackUnit.__init__(self, name, hp,0, damage)
#             Flyable.__init__(self,flying_speed)
#         def move(self, location):
#             print("[공중 유닛 이동]")
#             self.fly(self.name, location)
#
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False
#
#     def clocking(self):
#         if self.clocked == True:
#             print("{0}  클로킹 모드 해제".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드 설정".format(self.name))
#             self.clocked = True
#
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")
#
# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다")
#
# #실제 게임 진행
# game_start()
#
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()
#
# t1 = Tank()
# t2 = Tank()
#
# w1 = Wraith()
#
# #유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)
#
# #전군 이동
# for unit in attack_units:
#     unit.move("1시")
#
# #탱크 시즈모드
# Tank.seize_develped = True
# print("[알림] 탱크 시즈 모드 개발이 완료 되었습니다")
#
# #공격 모드 준비
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()
#
# #전군 공격
# for unit in attack_units:
#     unit.attack("1시")
#
# #전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,21)) #공격 랜덤
#
# #게임 종료
# game_over()

#퀴즈8
# import house as house
#
#
# class House:
#     def __init__(self,location,house_type,deal_type,price,completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
#
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)
#
# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
#
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)
#
# print("총 {0}대의 매물이 있습니다".format(len(houses)))
# for house in houses:
#     house.show_detail()

#모듈
# import theater_module
# theater_module.price(3) #3명이서 영화 보러갔을 때 가격
# theater_module.price_morning(4) #4명 조조 할인 영화 가격
# theater_module.price_soldier(5) #5명 군인 영화 가격

# import  theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7)

# from  theater_module import price_soldier as price
# price(5)

#패키지
# import travel.thailand
# import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import  vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

#__all__, 모듈 직접 실행
# from  random import *
# from  travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

#패키지, 모듈 위치
# import  inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

