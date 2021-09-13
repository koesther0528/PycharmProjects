from baseball_game_engine import make_answer, check

answer = make_answer()

# 숫자 물어보기
while True:
    guess = input("정답은?")
    # 숫자인지 아닌지 확인하자
    guess_int = int(guess)
    print(guess_int)

# strike, ball 판정하기
    strike, ball = check(guess, answer)

# 출력하기
    print(f'{guess}\tstrike: {strike}, ball: {ball}')

# 정답 == 숫자 끝내기
    if answer == guess:
        print('정답입니다!')
        break