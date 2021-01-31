 print("5. change 이름 : 해당 연락처의 정보 수정")

        print("6. delete 이름 : 해당 연락처 삭제")



    if command == 'add' :

        print("사용자를 추가합니다.")

        input_name = input("이름을 입력해 주세요. : ")

        input_phone = input("전화번호를 입력해 주세요. : ")

        input_email = input("이메일을 입력해 주세요. : ")

        input_address = input("주소를 입력해 주세요. : ")

        numbook[input_name] = '전화번호', input_phone, "이메일", input_email, "주소", input_address

        cnt = cnt + 1



    if command == 'all' :

        print("모든 사용자의 정보를 출력합니다.")

        numbooklist = []

        numbooklist = sorted(numbook.items(), key = operator.itemgetter(0))

        for j in range (0, cnt, 1) :

            print("이름 : ", *numbooklist[j])



    if command == 'quit' :

        i = 1



    if command == 'search' :

        command = input("검색할 사용자의 이름을 입력해 주세요. : ")

        if command in numbook :

            print("이름 : ", command, numbook[command])

        else :

            print("없는 사람입니다.")

        

    if command == 'change' :

        command = input("변경할 사용자의 이름을 입력해 주세요. : ")

        if command in numbook :

            input_name = input("변경할 이름을 입력해 주세요. : ")

            input_phone = input("변경할 전화번호를 입력해 주세요. : ")

            input_email = input("변경할 이메일을 입력해 주세요. : ")

            input_address = input("변경할 주소를 입력해 주세요. : ")

            numbook[input_name] = '전화번호', input_phone, "이메일", input_email, "주소", input_address

            del numbook[command]

        else :

            print("없는 사람입니다.")





    if command == 'delete' :

        command = input("삭제할 사용자의 이름을 입력해 주세요. : ")

        if command in numbook :

            del numbook[command]

            cnt = cnt - 1

        else :

            print("없는 사람입니다.")
