def add():
    name = str(input("이름을 입력해주세요: "))
    num = str(input("전화번호를 입력해주세요: "))
    e = str(input("email을 입력해주세요: "))
    addr = str(input("주소를 입력해주세요: "))
    contact.append(name)
    contact.append(num)
    contact.append(e)
    contact.append(addr)
    contact_list.append(contact)
    name_dic[name] = contact


def all():
    print("[이름, 전화번호, email, 주소] 순서입니다.")
    contact_list.sort()
    print(contact_list)


def search():
    search_name = str(input("검색할 이름을 입력해주세요: "))
    if search_name in name_dic:
        print(name_dic[search_name])
    else:
        print("검색한 이름이 연락처에 없습니다.")


def change():
    name = str(input("수정할 사람의 이름을  입력해주세요: "))
    if name in name_dic:
        contact_list.remove(name_dic[name])
        del name_dic[name]

        name = str(input("수정할 이름을 입력해주세요: "))
        num = str(input("수정할 전화번호를 입력해주세요: "))
        e = str(input("수정할 email을 입력해주세요: "))
        addr = str(input("수정할 주소를 입력해주세요: "))
        contact.append(name)
        contact.append(num)
        contact.append(e)
        contact.append(addr)
        contact_list.append(contact)

        name_dic[name] = contact

    else:
        print("수정할 사람이 연락처에 없습니다.")


def delete():
    name = str(input("삭제할 사람의 이름을  입력해주세요: "))
    contact_list.remove(name_dic[name])
    del name_dic[name]
    print(str(name) + "을 연락처에서 삭제했습니다.")


contact_list = []
name_dic = {}
while True:
    print("add    : 연락처 입력")
    print("all    : 연락처 출력")
    print("search : 연락처 검색")
    print("change : 연락처 수정")
    print("delete : 연락처 삭제")
    print("quit   : 종료")
    menu = str(input("메뉴선택: "))

    contact = []
    if menu == "add":
        add()

    elif menu == "all":
        all()

    elif menu == "search":
        search()

    elif menu == "change":
        change()

    elif menu == "delete":
        delete()

    elif menu == "quit":
        print("프로그램을 종료합니다.")
        break
