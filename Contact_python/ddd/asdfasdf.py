contact_list = [['a', 1, 2, 3, ], ['b', 2, 3, 4], ['c', 3, 4, 5]]

con_len = len(contact_list)
print(con_len)


contact_list[0]

for i in range(0, con_len):


search_name = 'b'

for i in range(0, con_len):
    if search_name == contact_list[i][0]:
        print(contact_list[i])

con_len = len(contact_list)
for i in range(0, con_len):
    if name == contact_list[i][0]:
        del contact_list[i]


contact_list = [['a', 1, 2, 3, ], ['b', 2, 3, 4], ['c', 3, 4, 5]]
con_len = len(contact_list)
name = str(input("삭제할 사람의 이름을  입력해주세요: "))

i = 0
while i < con_len:
    if name == contact_list[i][0]:
        del contact_list[i]
        print(str(name) + "을 연락처에서 삭제했습니다.")
        i = i + 1

        name = str(input("수정할 이름을 입력해주세요: "))
        num = str(input("수정할 전화번호를 입력해주세요: "))
        e = str(input("수정할 email을 입력해주세요: "))
        addr = str(input("수정할 주소를 입력해주세요: "))
        contact.append(name)
        contact.append(num)
        contact.append(e)
        contact.append(addr)
        contact_list.append(contact)

lst = [4, 3, 2, 3, 1]
for item in lst:
    if item == 3:
        lst.remove(3)

    elif menu == "d":
        name = str(input("삭제할 사람의 이름을  입력해주세요: "))
        a = 0
        j = 0
        doo = []
        for i in range(0, con_len):
            if name == contact_list[i][0]:
                contact_list[i]
                while j <= i-1:
                    doo.append(contact_list[j])
                    print(doo)
                    j = j + 1
                while j <= con_len:
                    doo.append(contact_list[j])
                    j + 1
                print(str(name)+" 님이 연락처에서 삭제되었습니다.")
                contact_list = doo
            else:
                a = a + 1
        if a == con_len:
            print(str(name)+" 님이 연락처에 없습니다.")
