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

class Address:
    # 주소의 클래스

    def __init__(self, name="무명씨"):
        # print("요녀석은 인스턴스를 만들때 실행됩니다.")
        self.__name = name
        self.__family_name = None
        self.__nick = None
        self.__email = None
        self.__phone = None
        self.__team = None
        self.__age = 1

    def name(self, name):
        self.__name = name
        return self

    def phone(self, phone):
        self.__phone = phone
        return self

    def email(self, email):
        self.__email = email
        return self

    def nick(self, nick):
        self.__nick = nick
        return self

    def team(self, team):
        self.__team = team
        return self

    def age(self, age):
        self.__age = age
        return self

    def __str__(self):
        return "이름 : %s | 닉네임 : %s | 전화 : %s" % (self.__name, self.__nick, self.__phone)




class AddressBook:
    """
    아래에 있는 Address는 잘못된 코드입니다.
    무엇이 잘못된 것입니다
    왜 잘못 됐는지 생각해보세요
    """
    addresses = []

    """
    list
    add list.append()
    remove remove
    index
    """

    def add(self, address=Address()):
        self.addresses.append(address)
        pass

    def delete(self, name_or_nick):
        result = self.search(name_or_nick)
        if result is not None:
            self.addresses.remove(result)
            print(name_or_nick, "을 삭제했습니다")


    def modify(self):
        pass


    def search(self, keyword):
        byNickResult = self.searchAddrByNick(keyword)
        if byNickResult is not None:
            return byNickResult

        return self.searchAddrByName(keyword)

    def searchAddrByNick(self, nick=None):
        # 이름으로 주소를 검색한다
        for addr in self.addresses:
            print(addr)
            if nick == addr.nick:
                return addr
        return None

    def searchAddrByName(self, name=None):
        # 이름으로 주소를 검색한다
        for addr in self.addresses:
            if name == addr.name:
                return addr
        return None


    def display(self):
        # 모든 주소 데이터를 출력하다
        print("===============================================")
        print("= TREENOD ADDRESS BOOK                        =")
        print("===============================================")
        for address in self.addresses:
            print(address)
        print("===============================================")

    def displayOne(self, name=None):
        # 이름으로 검색된 주소의 모든 데이터를 보여준다.
        pass


# 인스턴스를 만들어봅시다
# 클래스이름() 인스턴스화
simon = Address("원진").nick("싸이먼").phone("01033334444")
jessie = Address("진숙").nick("제시").phone("01055556666")
william = Address("신용").nick("윌리엄").phone("01066667777")


book = AddressBook()
book.add(simon)
book.add(jessie)
book.add(william)
book.add(Address("이기"))
book.add(Address("쿠쿠"))
book.add(Address("와프"))

# 주소록에 있는 모든 데이터를 보여준다
book.display()
book.delete("와프")
book.display()
