# 1,2,3 또는 "1", "2", "3"을 넣으면 "r", "s", "p"로 바꿔줍니다.
def intToRsp(rsp):
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
    elif p1 == "s" and com == "p":
        print("[p1 %s] vs [com %s] 승리" % (p1, com))
    elif p1 == "r" and com == "s":
        print("[p1 %s] vs [com %s] 승리" % (p1, com))
    elif p1 == "p" and com == "r":
        print("[p1 %s] vs [com %s] 승리" % (p1, com))
    else:
        print("[p1 %s] vs [com %s] 패배" % (p1, com))


# 반복문에는 for while 이 있구요. 오늘은 while만 배워봅시다.
# 요렇게 생겼습니다.
# while condition:
#     body

# while문 샘플입니다. 나는 천재다를 찍어봅시다.
def whileExample(ipt=100):
    x = 1
    while True:
        if x == ipt:
            break
        print("[%d]나는 천재다 " % x)
        x = x + 1


def inputExample():
    # input으로 받아오는 결과값은 문자열 타입입니다.
    ipt = input("숫자를 입력하세요. : ")

    # 숫자처럼 생긴 글자에 주의하세요.
    # 글자를 숫자로 변경할 때는 int(글자)로 감싸줍니다.
    print(type(ipt))
    print(1 == int("1"))

    whileExample(int(ipt))


from random import random
from math import ceil

# my = intToRsp(player1)
# com = intToRsp(computer)
computer = ceil(random() * 3)

# 입력을 받기위해서 input 사용
player1 = input("1,2,3 중에 하나만 입력하세요 : ")
rsp(player1, computer)  # r, s p