contact_list = []

while True:
    print("ad   : 연락처 입력")
    print("al   : 연락처 출력")
    print("s    : 연락처 검색")
    print("c    : 연락처 수정")
    print("d    : 연락처 삭제")
    print("quit : 종료")
    menu = str(input("메뉴선택: "))
    contact = []
    con_len = len(contact_list)

    if menu == "ad":
        name = str(input("이름을 입력해주세요: "))
        num = str(input("전화번호를 입력해주세요: "))
        e = str(input("email을 입력해주세요: "))
        addr = str(input("주소를 입력해주세요: "))
        contact.append(name)
        contact.append(num)
        contact.append(e)
        contact.append(addr)
        contact_list.append(contact)

    elif menu == "al":
        print("[이름, 전화번호, email, 주소] 순서입니다.")
        contact_list.sort()
        print(contact_list)

    elif menu == "s":
        name = str(input("검색할 이름을 입력해주세요: "))
        a = 0
        for i in range(0, con_len):
            if name == contact_list[i][0]:
                print(contact_list[i])
            else:
                a = a + 1
        if a == con_len:
            print(str(name)+" 님이 연락처에 없습니다.")

    elif menu == "c":
        name = str(input("수정할 사람의 이름을  입력해주세요: "))
        a = 0
        for i in range(0, con_len):
            if name == contact_list[i][0]:
                cg_l = contact_list[i]
                name = str(input("수정할 이름을 입력해주세요: "))
                num = str(input("수정할 전화번호를 입력해주세요: "))
                e = str(input("수정할 email을 입력해주세요: "))
                addr = str(input("수정할 주소를 입력해주세요: "))
                cg_l[0] = name
                cg_l[1] = num
                cg_l[2] = e
                cg_l[3] = addr
            else:
                a = a + 1
        if a == con_len:
            print(str(name)+" 님이 연락처에 없습니다.")

    elif menu == "d":
        name = str(input("삭제할 사람의 이름을  입력해주세요: "))
        try:
            i = 0
            a = 0
            while i <= con_len:
                if name == contact_list[i][0]:
                    # contact_list 에다가 바로 지우면 IndexError뜸 그래서 빈 리스트 하나 더 만들고 거기다 지움
                    doo = contact_list
                    doo.remove(doo[i])
                    print(str(name)+" 님이 연락처에서 삭제되었습니다.")
                    contact_list = doo
                    i = i + 100 + con_len*2
                else:
                    i = i + 1
                    a = a + 1
            if a == con_len:
                print(str(name)+" 님이 연락처에 없습니다.")
        except IndexError:
            print("등록된 연락처가 없습니다.")

    elif menu == "quit":
        print("프로그램을 종료합니다.")
        break
