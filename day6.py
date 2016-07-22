# if elif else 를 배우자
"""
if condition:
    body
elif condition2:
    body2
elif condition3:
    body3
else:
    default
"""


def ageTest():
    age = 36
    misung = 19

    if age < misung:
        print("미성년자입니다.")
    else:
        print("어른입니다.")


"""
print 할때 변환
%d : digit의 약자 즉 숫자이다.
%s : string의 약자 즉 문자열이다.
"""


def timeTest(time):
    if time < 12:
        print("%d시는 오전입니다." % time)
    elif time == 12:
        print("%d시는 정오입니다." % time)
    else:
        print("%d시는 오후입니다." % time)


# 반복문 for, while
# for x in range(24):
#     time = x + 1
#     timeTest(time)

# print (list(range(24)))

"""
가위바위보
1인용 게임
player vs computer
가위  가위
가위  바위
가위  보

바위  가위
바위  바위
바위  보

보   가위
보   바위
보   보
"""


# scissors, rock, paper
def rsp(p1, com):
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


# def testRSP():
#     rsp("s", "s")
#     rsp("s", "r")
#     rsp("s", "p")
#
#     rsp("r", "s")
#     rsp("r", "r")
#     rsp("r", "p")
#
#     rsp("p", "s")
#     rsp("p", "r")
#     rsp("p", "p")

testList = \
    [("s", "s"),
     ("s", "r"),
     ("s", "p"),
     ("r", "s"),
     ("r", "r"),
     ("r", "p"),
     ("p", "s"),
     ("p", "r"),
     ("p", "p")]

for x, y in testList:
    rsp(x, y)