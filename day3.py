"""
def define 정의하다
무엇을? 함수

이름 (입력=기본값, 입력2=기본값2, 입력3=기본값3):
   return 출력, 출력2, 출력3

def something (input):
    // something doing
    return output
"""


def something(input="default"):
    # something doing
    output = "blahblah"
    return output


def hello(name="world"):
    return "hello %s" % name


def printSum(a, b):
    print("total ", add(a, b))


def add(a, b):
    return a + b


# 빼기
def sub(a, b):
    return a - b


# 곱하기
def mul(a, b):
    return a * b


# 나누기
def div(a, b):
    return a / b


# 나머지
def rest(a, b):
    return a % b


# 제곱?
def square(a):
    # return a ** 2
    return pow(a, 2)


def pow(a, n):
    return a ** n


# 한글로 함수명을 정의 할 수 있지만, 추천하지는 않습니다..^^;
def 더하기(a, b):
    print("더하기 결과 : ", a + b)


더하기(2, 3)


def day4example():
    a = 10
    b = 30
    print("%d + %d =" % (a, b), add(a, b))
    print("%d - %d =" % (a, b), sub(a, b))
    print("%d * %d =" % (a, b), mul(a, b))
    print("%d / %d =" % (a, b), div(a, b))
    print("%d ** %d =" % (a, 4), pow(a, 4))
    print("%d %% %d =" % (b, a), rest(b, a))
    print("%d의 제곱 = " % a, square(a))


day4example()