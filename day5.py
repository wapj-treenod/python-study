from random import random
from math import ceil

# 가위바위보 게임

"""
expression 표현식

a == b
name == "wapj"


boolean True / False
"""


def ifBooleanExample():
    isMonday = True
    condition = (isMonday == True)
    if condition:
        print("피곤하다")

    if isMonday is True:
        print("진짜 피곤하다")

    if isMonday != False:
        print("겁나 피곤하다")

    if isMonday is not False:
        print("전혀 피곤하지 않은 것이 아니다")


def ifIntExample():
    isYoung = 19
    myAge = 35
    if myAge > isYoung:
        print("미성년자가 아닙니다.")

    jonathanAge = 19

    if jonathanAge > isYoung:
        print("조나단은 미성년자가 아닙니다")
    else:
        print("조나단은 미성년자 입니다.")


"""
가위바위보 규칙
1. 같은게 나오면 비긴다
2. 바위는 가위에게 이긴다.
3. 가위는 보에게 이긴다.
4. 보는 바위에게 이긴다.
5. 나머지 경우는 진 경우이다.

a   b
가위 가위
가위 바위
가위 보

바위 가위
바위 바위
바위 보

보   가위
보   바위
보   보
"""


### 이긴경우는 1, 비긴경우는 0, 진경우는 -1을 각각 리턴한다
def rsp(a, b):
    rock = "바위"
    scissors = "가위"
    paper = "보"

    ## a기준으로 작성
    if a == b:
        print("%s vs %s %s가 비겼습니다." % (a, b, a))
    elif a == scissors and b == rock:
        print("%s vs %s %s가  졌습니다." % (a, b, a))
    elif a == scissors and b == paper:
        print("%s vs %s %s가  이겼습니다." % (a, b, a))
    elif a == rock and b == scissors:
        print("%s vs %s %s가  이겼습니다." % (a, b, a))
    elif a == rock and b == paper:
        print("%s vs %s %s가  졌습니다." % (a, b, a))
    elif a == paper and b == scissors:
        print("%s vs %s %s가  졌습니다." % (a, b, a))
    elif a == paper and b == rock:
        print("%s vs %s %s가  이겼습니다." % (a, b, a))
    return 1


a = "가위"
b = "바위"

rsp(a, b)
# myInput = input("""[1],[2],[3]중에 하나만 선택하시오
# 1. 가위
# 2. 바위
# 3. 보
# """)
# print(myInput)


print(ceil(random() * 3))