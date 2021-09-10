# 정답 만들기(0~9까지 숫자 3개 뽑기)
import random

def make_answer():
    list = random.sample(range(9+1),3)
    return "".join(map(str, list))

def check(guess, answer):
    strike = 0
    ball = 0
    # 숫자 하나 꺼내서 정답에 있고, 자리가 같으면 strike += 1
    # 숫자 하나 꺼내서 정답에 있고, 자리가 다르면 ball += 1
    for i in range(3):
        for j in range(3):
            if guess[i] == answer[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1

    return strike, ball

if __name__ == '__main__':
    answer = make_answer()
    print(answer)
    strike, ball = check("832", "934")
    print(strike, ball)
    strike, ball = check("432", "934")
    print(strike, ball)
    strike, ball = check("934", "934")
    print(strike, ball)