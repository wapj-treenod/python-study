"""
연락처를 만들어보자
들어가는 데이터

1. 성
2. 이름
3. 전화번호
4. 이메일
5. 닉네임
6. 팀

kuku
iggy
william
"""

kuku = {
    'family_name': "김",
    'first_name': "상미",
    'phone': "01011112222",
    'email': "kuku@treenod.com",
    'nick': "kuku",
    'team': "pokopang"
}

iggy = {'family_name': "김",
        'first_name': "가람",
        'email': "iggy@treenod.com",
        'nick': "iggy",
        'phone': "01033334444",
        'age': 18,
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


name = "가람"
for item in address_dict.items():
    _name = get_name(item["nick"])
    if name == _name:
        print(item["nick"])



