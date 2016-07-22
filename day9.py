# 반복문

### while / for

"""
condition 을 만족하는 동안 계속 실행
while condition:
    print("blahblah")
"""

def whileExample():
    x = 0
    while x < 10:
        print(x)
        x += 1

# list, tuple, dictionary
def listExample():
    list_a = [1,2,3]

    # 수정
    list_a[0] = 10

    # 추가
    list_a.append(4)

    # 삭제
    del list_a[0]
    for x in list_a:
        print(x)


def tupleExample():
    # 튜플은 읽기전용입니다
    tuple_a = (1,2,3)
    for x in tuple_a:
        print(x)


def dictExample():
    dict_a = {"korea":"한국",
              "america": "미국",
              "japan":"일번"}

    ## 수정
    dict_a["japan"] = "일본"

    ## 추가
    dict_a["china"] = "중국"

    ## 삭제
    del dict_a["america"]

    for key, value in dict_a.items():
        print(key, value)


# dictExample()
# listExample()
"""
숙제
1. 반복문으로 아래와 같은 그림을 그리세요
*
**
***
****
*****
******

2. 반복문으로 1부터 100까지 더하는 함수를 만드세요.

3. 딕셔너리를 사용해서 키는 이름을 넣고,
값에는 전화번호를 넣어 보세요.
"""

def sum():
    sumVal = 0
    for x in list(range(101)):
        print(x + 1)
    return sumVal



# print("*" * 1)
# print("*" * 2)
# print("*" * 3)
# print("*" * 4)
# print("*" * 5)
#
# for x in range(1, 6):
#     print("*" * x)


# sum = 0
# for x in range(1, 101):
#     sum += x
# print(sum)

## 수학공식
def sum100(n=100):
    n = n * (n + 1) / 2
    print(n)

#sum100()

phoneBook = {}
phoneBook['wapj'] = "01051775141"
phoneBook["max"] = "01012345678"

print(phoneBook['wapj'])