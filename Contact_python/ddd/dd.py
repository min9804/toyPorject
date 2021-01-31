
user = []


def start():

    while True:
        num = int(
            input("\n연락처 메뉴 [1.등록   2.조회   3.삭제   4.출력  5.수정  6.종료]   선택 = "))
        if num == 1:
            print("\n================= 연락처 등록 ================")
            user.append(Address())
        elif num == 2:
            name = input("조회할 이름을 입력하세요 : ")
            print("\n================= 연락처 조회 ================")
            if not user_print(name):
                print("\n조회 결과가 없습니다.")
        elif num == 3:
            print("\n================= 연락처 삭제 ================")
            name = input("\n삭제할 이름을 입력하세요 : ")
            if user_print(name):
                delnum = int(input("\n삭제할 번호를 입력하세요 :"))
                del(user[delnum-1])
                print("\n삭제되었습니다.")
        elif num == 4:
            print("\n================= 연락처 전체 조회 ================")
            if len(user) != 0:
                user_print("all")
            else:
                print("\n조회 결과가 없습니다.")
        elif num == 5:
            print("\n================= 연락처 수정 ================")
            name = input("\n변경할 이름을 입력하세요 : ")
            if user_print(name):
                delnum = int(input("\n변경할 번호를 입력하세요 :"))
                chnum = int(input("\n변경할 항목 선택 (1. 이름, 2. 전화번호, 3.이메일) : "))
                if chnum == 1:
                    user[delnum-1].setname(input("변경 이름 : "))
                elif chnum == 2:
                    user[delnum-1].settell(input("변경 전화번호 : "))
                elif chnum == 3:
                    user[delnum-1].setemail(input("변경 이메일 : "))
                else:
                    print("\n잘못입력하셨습니다")
            else:
                print("\n변경할 이름이 없습니다.")
        elif num == 6:
            break
        else:
            print("다시 입력하세요")


def user_print(name):
    if name == "all":
        for i in range(0, len(user)):
            print(i+1, end=" ")
            user[i].disp()
        return
    else:
        for i in range(0, len(user)):
            if user[i].name == name:
                print(i+1, end=" ")
                user[i].disp()
        return True
    return False


class Address:
    def __init__(self):
        self.name = input("이름 입력 : ")
        self.tell = input("전화번호 입력 :")
        self.email = input("이메일 입력 :")

    def setname(self, name):
        self.name = name

    def settell(self, tell):
        self.tell = tell

    def setemail(self, email):
        self.email = email

    def disp(self):
        print(self.name, " ", self.tell, " ", self.email)


if __name__ == "__main__":
    start()
