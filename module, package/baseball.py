from baseball_game_engine import make_answer, check

answer = make_answer()

# 숫자 물어보기
while True:
    guess = input("정답은?")
    # 숫자인지 아닌지 확인하자
    try:
        guess_int = int(guess)
    except ValueError as e:
        print('숫자를 입력하세요.')
        continue
    if len(guess) != len(answer):
        raise InvalidlengthError('정답의 길이와 다릅니다.')



# strike, ball 판정하기
    strike, ball = check(guess, answer)

# 출력하기
    print(f'{guess}\tstrike: {strike}, ball: {ball}')

# 정답 == 숫자 끝내기
    if answer == guess:
        print('정답입니다!')
        break