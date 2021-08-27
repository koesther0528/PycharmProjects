#1-1
# id_number = "040528"
# print(id_number[0:2])
# print(id_number[2:6])
# print(int(id_number[0:2]) + int(id_number[2:6]))
#
# print("\n")
#
# #1-2
# phone_number = "02-1234-5678".split("-")
# print(phone_number[0] + "\n" + phone_number[2])

#2-1
# student_number='2401'
# if student_number[1]=="1":
#     print("1반 뉴미디어소프트웨어과")
# elif student_number[1]=="2":
#     print("2반 뉴미디어소프트웨어과")
# elif student_number[1]=="3":
#     print("3반 뉴미디어웹솔루션과")
# elif student_number[1]=='4':
#     print("4반 뉴미디어웹솔루션과")
# elif student_number[1]=='5':
#     print("5반 뉴미디어디자인과")
# elif student_number[1]=="6":
#     print("6반 뉴미디어디자인과")
# else:print("잘못입력했습니다.")

#2-2
# def get_major(argumenet):
#     if argumenet[1]=="1" or argumenet[1]=="2":
#         major="뉴미디어소프트웨어과"
#         return argumenet[0],major
#     elif argumenet[1]=="3" or argumenet[1]=="4":
#         major="뉴미디어웹솔루션과"
#         return argumenet[0],major
#     elif argumenet[1]=="5" or argumenet[1]=="6":
#         major="뉴미디어디자인과"
#         return argumenet[0],major
#
# grade,major=get_major("2401")
# print(major,grade)

#2-3
# def average(*number):
#     sum=0
#     for i in number:
#         sum+=i
#         i+=1
#     average=(sum/len(number))
#     print(average)
#
#
# print(average(10,20,30))

#2-4
# def get_bmi(height, weight):
#     height/=100
#     bmi=round((weight/(height*height)),1)
#     if bmi>18.5:
#         return "저체중"
#     elif bmi>=18.5 and bmi<23:
#         return "보통"
#     elif bmi>=23 and bmi<25:
#         return "과체중"
#     elif bmi >25:
#         return "비만"
#
# bmi=get_bmi(176,69)
# print(bmi)

#3-1
# def n_sum(n):
#     new = str(n)
#     add = 0
#     if n >= 1000000000:
#         return -1
#     for i in range(len(new)):
#         add += int(new[i])
#     return add
#
# result = n_sum(10)
# print(result)        #1
# result = n_sum(331)
# print(result)         #7
# result = n_sum(408)
# print(result)         #12
# result = n_sum(1000000000)
# print(result)         #-1

#3-2
# import math
# def get_subway_fare(km):
#     if km < 10:
#         pay = 720
#         return pay
#     if km < 50 :
#         pay = 720
#         add = math.ceil((km-10)/5)
#         for i in range(add):
#             pay += 100
#         return pay
#     if km > 50 :
#         pay = 1520
#         add = math.ceil((km-50)/8)
#         for i in range(add):
#             pay+= 100
#         return pay
#
# fare = get_subway_fare(5)
# print(fare)        #720
# fare = get_subway_fare(26)
# print(fare)        #1120
# fare = get_subway_fare(61)
# print(fare)        #1720

#3-3
# def get_three_six_nine(num):
#     s_sum=str(num)
#     result = ""
#     cont = (s_sum.count('3')+s_sum.count('6')+s_sum.count('9'))
#     if cont <= 0:
#         result = s_sum
#     else:
#         for j in range(cont) :
#             result += "짝"
#     return result
#
# result = get_three_six_nine(1)
# print(result)        #1
# result = get_three_six_nine(3)
# print(result)        #짝
# result = get_three_six_nine(16)
# print(result)        #짝
# result = get_three_six_nine(36)
# print(result)        #짝짝

#3-4
#소수인지 아닌지 알 수 있는 함수 만들기
# def PrimeNumber(j):
#     if j == 1:
#         return False
#     j_root = round(j ** 0.5) + 1
#     for i in range(2, j_root):
#         if not (j % i):
#             return False
#     return True
#
# num = int(input())
# if PrimeNumber(num):
#     print("소수")
# else:
#     print("소수 아님")

#4-1
#소수 판별하기
# def is_prime(number):
#     if number != 1:
#         for i in range(2,number):
#             if number % i == 0:
#                 return "소수 아님"
#             else:
#                 return "소수"
#         return "소수"
#
# result = is_prime(2)
# print(result)     #소수
# result = is_prime(13)
# print(result)     #소수
# result = is_prime(36)
# print(result)     #소수 아님

#4-2
# def get_compliment(n):
#     if '고구마' in n:
#         return ('왓쇼이!')
#     elif '맛있는' in n:
#         return ('우마이!')
#     elif '놀랄 만한' in n:
#         return ('요모야!')
#     elif '황당한' in n:
#         return ('요모야!')
#     elif '굉장한' in n:
#         return ('요모야!')
#     else:
#         return ("으무!")
#
# result = get_compliment('고구마 된장국')
# print(result) # 왓쇼이!
# result = get_compliment('맛있는 크레이프')
# print(result) # 우마이!
# result = get_compliment('놀랄 만한 상황')
# print(result) # 요모야..!
# result = get_compliment('좋은 마음가짐이다!')
# print(result) # 으무!

#5-1
#필요한것끼리 묶음처럼 잘 만들어진 파일, 함수나 클래스등의 파이썬 문장들을 담고있는 파일, 확장자 .py

#5-2
#모듈들을 모아놓은 집합, 하나의 디렉토리의 여러 모듈 파일들을 갖다놓은 것

#5-3
#import theater_module as p2401
## from theater_module import price as p2401

#5-4
#패키지 안에 포함된것중에 import 되길 원하는 것은 공개로 하고 원하지않은 것은 비공개로 돌릴 수 있는 것

#5-5
#if __name__

#5-6
#<가>
# import travel.vietnam
# import travel.vietnam.VietnamPackage
# trip_to = travel.vietnam.VietnamPackage()
# trip_to.detail()
#<나>
# from travel import  vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
#<다>
# from travel.vietnam import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()