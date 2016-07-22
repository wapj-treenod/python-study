from random import random
from math import ceil


def returnThree(x, y, z):
    """
    리턴값을 여러개를 지정할 수 있습니다.
    받을 때에도 변수 여러개를 콤마(,)로 구분해서 지정하면 됩니다.
    리턴되는 변수의 갯수와 받는 변수의 갯수는 동일해야 합니다.
    """
    return x, y, z

a, c, b = returnThree(3, 4, 5)

print(a, b, c)

"""
for또한 반복문입니다. 반복되는 조건은 여러개가 들어 있는 녀석을 넣어주면 갯수만큼 뺑뺑이를 돌립니다.
아래 함수에서는 iterable이 여러개가 들어 있는 녀석입니다.
1부터 10까지 반복하는 녀석을 만들어보면 아래와 같습니다.

for x in iterable:
    print(x)

"""
for x in range(10):
    print(x + 1)

"""
standard input
standard output
"""


def testInput():
    str = input("문자열 : ")

    print("type : ", type(str))

    print("1 == '1'", 1 == str)

    ## 문자를 숫자로 바꾸는 법 int(문자열)
    print("1 == int('1')", 1 == int(str))
    print("str : ", str)


def intToRsp(rsp):
    """
    1,2,3 입력을 받음
    1인 경우는 s: 가위
    2인 경우는 r: 바위
    그외는 보
    """
    if int(rsp) == 1:
        return "s"
    elif int(rsp) == 2:
        return "r"
    else:
        return "p"


# scissors, rock, paper 가위, 바위, 보 로직 함수
def rsp(p1, com):
    p1 = intToRsp(p1)
    com = intToRsp(com)
    if p1 == com:
        print("[p1 %s] vs [com %s] 비김" % (p1, com))
        return 0, 1, 0
    elif p1 == "s" and com == "p":
        print("[p1 %s] vs [com %s] 승리" % (p1, com))
        return 1, 0, 0
    elif p1 == "r" and com == "s":
        print("[p1 %s] vs [com %s] 승리" % (p1, com))
        return 1, 0, 0
    elif p1 == "p" and com == "r":
        print("[p1 %s] vs [com %s] 승리" % (p1, com))
        return 1, 0, 0
    else:
        print("[p1 %s] vs [com %s] 패배" % (p1, com))
        return 0, 0, 1


round = 3
vic, drw, lose = 0, 0, 0  # 초기화
for x in range(round):
    print("%d 판 시작합니다." % (x + 1))
    v = input("1,2,3중에 하나만 입력하세요 : ")
    c = ceil(random() * 3)
    # print(intToRsp(v) + " vs " + intToRsp(c))
    v, d, l = rsp(v, c)
    print(v, d, l)
    vic += v
    drw += d
    lose += l

print("전적 : %d승 %d패 %d무" % (vic, drw, lose))

