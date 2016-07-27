"""
연락처를 만들어보자
들어가는 데이터

연락처
1. 성
2. 이름
3. 전화번호
4. 이메일
5. 닉네임
6. 팀

=> 클래스로 만들어봅시다
"""


class AddressBook:
    """
    아래에 있는 Address는 잘못된 코드입니다.
    무엇이 잘못된 것입니다
    왜 잘못 됐는지 생각해보세요
    """
    Address = None # 아래에 있는 주소가 들어갑니다

    def add(self):
        pass

    def modify(self):
        pass

    def delete(self):
        pass

    def search(self):
        pass



class Address:
    # 주소의 클래스
    family_name = None
    name = None
    phone = None
    email = None
    nick = None
    team = None
    age = 0

    def __init__(self, name="바보야 이름을 적으라고"):
        # print("요녀석은 인스턴스를 만들때 실행됩니다.")
        self.name = name

    def __str__(self):
        return "이름 : %s | 닉네임 : %s | 전화 : %s\n" % (self.name, self.nick, self.phone)


    def eat(self):
        return "%s(은)는 밥을 먹습니다\n" % self.nick




# 인스턴스를 만들어봅시다
# 클래스이름() 인스턴스화
simon = Address("원진")
simon.nick = "싸이먼"
simon.phone = "01033334444"

jessie = Address("진숙")
jessie.nick = "제시"
jessie.phone = "01055556666"

william = Address("신용")
william.nick = "윌리엄"
william.phone = "01066667777"

print(simon, jessie, william)

print(simon.eat())
print(jessie.eat())
print(william.eat())

def temp():
    kuku = {
        'family_name': "김",
        'first_name': "상미",
        'phone': "01011112222",
        'email': "kuku@treenod.com",
        'nick': "kuku",
        'age': 18,
        'team': "pokopang"
    }

    iggy = {
        'family_name': "김",
        'first_name': "가람",
        'email': "iggy@treenod.com",
        'nick': "iggy",
        'phone': "01033334444",
        'team': "dice"
    }

    william = {
        'family_name': "강",
        'phone': "01044445555",
        'email': "william@treenod.com",
        'first_name': "신용",
        'nick': "william",
        'team': "quest"
    }


    address = [kuku, iggy, william]

    address_dict = {"kuku":kuku,
                    "iggy":iggy,
                    "william":william}

    # 닉네임으로 이름을 알고 싶어요.
    def get_fullname(nick):
        full_name = address_dict[nick]["family_name"] + \
                    address_dict[nick]["first_name"]
        return full_name


    def get_name(nick):
        return address_dict[nick]["first_name"]


    get_fullname("iggy")
    get_fullname("william")
    get_fullname("kuku")



