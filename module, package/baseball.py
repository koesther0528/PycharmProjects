from baseball_game_engine import make_answer, check

answer = make_answer()
count = 0
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
        print(f'정답의 길이와 다른 것을 입력했습니다.{len(answer)} 문자')
        continue



# strike, ball 판정하기
    strike, ball = check(guess, answer)
    count += 1

# 출력하기
    print(f'{guess}\tstrike: {strike}, ball: {ball}\t{count}try')

# 정답 == 숫자 끝내기
    if answer == guess:
        print('정답입니다!')
        break