from random import random
from math import floor


def yagu_maker():
    # 중복없는 3개의 숫자 만들기
    l = []
    while len(l) < 3:
        r = str(floor(random() * 10))
        if r not in l:
            l.append(r)

    _yagu = "".join(l)
    return _yagu


def yagu_checker(my_yagu, yagu):
    """
    내가 입력한 my_yagu와 컴퓨터로 받은 yagu를 체크한 다음
    볼/스크라이크를 표시해줌
    인덱스와 숫자도 맞으면 스크라이크 숫자만 맞으면 볼
    """
    strike = 0
    ball = 0
    # 같은 자리에 있으면 스크라이크로 체크
    for idx, val in enumerate(yagu):
        # print(idx + 1, val)
        if my_yagu[idx] == val:
            strike += 1

    # 있으면 볼
    for my in my_yagu:
        if my in yagu:
            ball += 1

    result = (strike, ball - strike)

    return result


def play_game():
    print("============================")
    print("야구게임을 시작합니다")
    print("============================")
    yagu = yagu_maker()
    while True:
        my_yagu = input("숫자 3개를 입력하세요 : ")
        if len(my_yagu) < 3:
            print("잘못된 숫자입니다 다시 입력하세요.")
            continue

        result = yagu_checker(my_yagu, yagu)
        if result[0] == 3:
            print("당신이 이겼습니다. you win")
            exit(0)
        else:
            print("%s스크라이크 %s볼" % (result[0], result[1]))

if __name__ == "__main__":
    play_game()
