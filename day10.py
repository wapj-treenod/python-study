"""
숙제
1. 숫자 두개를 입력받아서 해당 숫자의 구구단을 출력하는 함수를 만들어보세요
ex ) gugu(3, 5)
3 x 1 =  3    4 x 1 =  4    5 x 1 =  5
3 x 2 =  6    4 x 2 =  8    5 x 2 = 10
3 x 3 =  9    4 x 3 = 12    5 x 3 = 15
3 x 4 = 12    4 x 4 = 16    5 x 4 = 20
3 x 5 = 15    4 x 5 = 20    5 x 5 = 25
3 x 6 = 18    4 x 6 = 24    5 x 6 = 30
3 x 7 = 21    4 x 7 = 28    5 x 7 = 35
3 x 8 = 24    4 x 8 = 32    5 x 8 = 40

2. 별그리기
******
*****
****
***
**
*
"""

def gugu(start=2, end=9, x_start=1, x_end=9, padding=3):
    for x in range(x_start, x_end+1):
        for y in range(start, end+1):
            print("%2d x %2d = %3d" % (y, x, x * y), end=" " * padding)
        print()


if __name__ == "__main__":
    gugu(3, 5, 1, 20)
    gugu(x_start=1, x_end=50, start=1, end=5)
    pass


def reverse_star():
    for x in reversed(range(1, 6)):
        print("*" * x)


def reverse_star2():
    len = 6
    while len > 0:
        print("*" * len)
        len -=1
