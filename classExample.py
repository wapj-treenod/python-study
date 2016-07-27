"""
클래스에 대해서 알아봅시다

클래스는 실제세계의 사물을 추상화 한 개념입니다.
추상화의 반대는 구체화 인데요.
구체적인 사례들을 모아서 공통된 요소들을 뽑아낸 것이 추상화 입니다.

예를 하나 들어보죠.

요크셔 테리어
시츄
말티즈
웰시코기
포메라니안
푸들
퍼그

위에 있는 녀석들을 하나로 묶을 수 있는 이름이 무엇이 있을까요?

강아지
------------------------
속성들
- 이름
- 종
- 털색
- 몸무게
- 평균수명
- 다리길이
- 꼬리길이
- 귀생김새
------------------------
행동들
- 짓는다
- 먹는다
- 잔다
- 반긴다
- 꼬리를 흔든다
"""


"""
클래스 이름은 대문자로 시작하는 것이 관례입니다.
"""
class Dog:
    name = None
    color = None
    weight = None

    def __init__(self):
        print("생성!")


    def __init__(self, name, color, weight):
        print("생성2!")
        self.name = name
        self.color = color
        self.weight = weight


    def bark(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    # def __str__(self):
    #     return self.name + "," + self.color + "," + self.weight


# 인스턴스를 만들어줌
dog = Dog("말티즈", "흰색", "9.8")
# dog2 = Dog()
# dog2.name = "말티즈"
# dog2.color = "흰색"
# dog2.weight = "9.8kg"

#기본값은 메모리 주소를 알려줍니다
print(dog)
# print(dog2)



class name:
    def __init__(self):
        pass

    def method1(self, param1):
        pass

    def method2(self, param2):
        pass


"""
숙제: 클래스를 인스턴스로 만들어서 print 문으로 찍어봅시다
"""