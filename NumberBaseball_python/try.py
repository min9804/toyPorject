# select_numbers = [1, 2, 3]
# guess = [6, 6, 6]

# for i in range(0, 3):
#     if guess[i] == select_numbers[i]:
#         st_count = st_count + 1
#     elif guess[i] in select_numbers:
#         ba_count = ba_count + 1
#     else:
#         ou_count = ou_count + 1


# print("공격 순서를 정합니다.")

# user_abc = set(input("가위~바위~보!!!: "))
# user_abc = 0
# if user_abc == "가위":
#     user_abc = 0
# elif user_abc == "바위":
#     user_abc = 1
# elif user_abc == "보":
#     user_abc == 2

# abc = random.randrange(0, 3)
# if abc == 0:
#     print("가위")
# elif abc == 1:
#     print("바위")
# elif abc == 2:
#     print("보")


# import random


# def rcp():
#     t = 0
#     while t == 0:
#         com = random.choice(["가위", "바위", "보"])
#         user = input("가위~바위~보!!: ")

#         winner = None
#         if com == "가위":
#             if user == "가위":
#                 winner = None
#             elif user == "바위":
#                 winner = "user"
#             else:
#                 winner = "computer"
#         elif com == "바위":
#             if user == "가위":
#                 winner = "computer"
#             elif user == "바위":
#                 winner = None
#             else:
#                 winner = "user"
#         else:
#             if user == "가위":
#                 winner = "user"
#             elif user == "바위":
#                 winner = "computer"
#             else:
#                 winner = None

#         if winner == "computer":
#             print("컴퓨터: ", com)
#             print("사용자: ", user)
#             print("승자 : ", "컴퓨터")
#             t = 1
#         elif winner == "user":
#             print("컴퓨터: ", com)
#             print("사용자: ", user)
#             print("승자 : ", "사용자")
#             t = 2
#         else:
#             print("컴퓨터: ", com)
#             print("사용자: ", user)
#             print("승자 : ", "무승부")
#             t = 0


# rcp()
# num = 0
# g = 0
# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num_list:
#     if num == num_list[i]:
#         g = g + 1

# a = 1
# if a != 2:
#     print('p')


# def user_defence():

# def user_defence():
#     num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     t = 0
#     g = 0
#     while g != 3:
#         while t <= 2:
#             g = 0
#             t = 0
#             user_select_numbers = []
#             print("수비수를 골라주세요.")
#             for i in range(0, 3):
#                 if i == 0:
#                     num = input("첫 번째 수비수를 입력하세요: ")
#                     for n in range(0, 10):
#                         if num == num_list[n]:
#                             g = g + 1
#                     user_select_numbers.append(num)
#                 elif i == 1:
#                     num = input("두 번째 수비수를 입력하세요: ")
#                     for n in range(0, 10):
#                         if num == num_list[n]:
#                             g = g + 1
#                     user_select_numbers.append(num)
#                     if num != user_select_numbers[0]:
#                         t = t + 1
#                 elif i == 2:
#                     num = input("세 번째 수비수를 입력하세요: ")
#                     for n in range(0, 10):
#                         if num == num_list[n]:
#                             g = g + 1
#                     user_select_numbers.append(num)
#                     if num != user_select_numbers[0]:
#                         t = t + 1
#                     if num != user_select_numbers[1]:
#                         t = t + 1
#             if g != 3:
#                 print("0~9사이의 숫자를 입력해 주세요.")
#                 t = t - 3
#             elif t <= 2:
#                 print("중복된 수를 선택할 수 없습니다.")
#             elif t == 3:
#                 for k in range(0, 3):
#                     n = user_select_numbers[k]
#                     n = int(n)
#                     user_select_numbers[k] = n
#                 print("당신의 수비수:", user_select_numbers)

# t = 0
# while t < 3:
#     t = 0
#     num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     user_select_numbers = []
#     for i in range(1, 4):
#         num = input(" %s 번째 수비수를 입력하세요: " % str(i))
#         if num in num_list:
#             num_list.remove(num)
#             user_select_numbers.append(num)
#             t = t + 1
#         elif num in user_select_numbers:
#             t = t - 100
#         else:
#             t = t - 1000
#     if t == 3:
#         for i in range(0, 3):
#             n = user_select_numbers[i]
#             n = int(n)
#             user_select_numbers[i] = n
#         print("당신의 수비수:", user_select_numbers)
#     elif -500 < t < 0:
#         print("중복된 수를 선택할 수 없습니다.")
#     elif t < -500:
#         print("0~9사이의 숫자를 입력해 주세요.")

# t = 0
# while t < 3:
#     t = 0
#     num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     guess = []
#     for i in range(1, 4):
#         num = input(" %s 번째 공격수를 입력하세요: " % str(i))
#         if num in num_list:
#             num_list.remove(num)
#             guess.append(num)
#             t = t + 1
#         elif num in guess:
#             t = t - 100
#         else:
#             t = t - 1000
#     if t == 3:
#         for i in range(0, 3):
#             n = guess[i]
#             n = int(n)
#             guess[i] = n
#         print("당신의 공격수:", guess)
#     elif -500 < t < 0:
#         print("중복된 수를 선택할 수 없습니다.")
#     elif t < -500:
#         print("0~9사이의 숫자를 입력해 주세요.")


# def guess_del_write():
#     x_count = 0
#     for i in range(0, 3):
#         for j in range(0, len(numbers)):
#             if guess[i] == numbers[j]:
#                 numbers[j] = "x"
#                 x_count = x_count + 1
#     for i in range(0, x_count):
#         numbers.remove("x")
#     for i in range(0, 3):
#         numbers.append(guess[i])


# def computer_attack():
#     global numbers
#     global q
#     global st_count
#     global ba_count
#     global ou_count
#     while len(numbers) != 3:
#         st_count = 0
#         ba_count = 0
#         ou_count = 0
#         t = 0
#         while t == 0:
#             # 컴퓨터 공격수 뽑기 셔플
#             random.shuffle(numbers)
#             guess = []
#             for i in range(0, 3):
#                 guess.append(numbers[i])
#             if guess[0] != guess[1]:
#                 if guess[0] != guess[2]:
#                     if guess[1] != guess[2]:
#                         t = t + 1
#             print("컴퓨터의 수", numbers)
#             print("컴퓨터가 뽑은수", guess)
#             q = q + 1
#             print(q, "회차")

#         # 점수판정
#         for i in range(0, 3):
#             if guess[i] == user_select_numbers[i]:
#                 st_count = st_count + 1
#             elif guess[i] in user_select_numbers:
#                 ba_count = ba_count + 1
#             else:
#                 ou_count = ou_count + 1


#         # 점수기반 전략 알고리듬
#         if ba_count == 3:
#             numbers = guess
#         elif ou_count == 3:
#             x_count = 0
#             for i in range(0, 3):
#                 for j in range(0, len(numbers)):
#                     if guess[i] == numbers[j]:
#                         numbers[j] = "x"
#                         x_count = x_count + 1
#             for i in range(0, x_count):
#                 numbers.remove("x")
#         elif st_count == 1:
#             if ba_count == 2:
#                 numbers = guess
#         print_count()

#     num_list_len = len(numbers)

#     while num_list_len == 3:
#         a = guess[0]
#         b = guess[1]
#         c = guess[2]

#         ghgh = 0
#         while ghgh < 7:
#             ghgh = ghgh + 1
#             st_count = 0
#             ba_count = 0
#             ou_count = 0
#             if ghgh == 0:
#                 guess[0] = a
#                 guess[1] = b
#                 guess[2] = c
#                 print(guess)
#             elif ghgh == 1:
#                 guess[0] = a
#                 guess[1] = c
#                 guess[2] = b
#                 print(guess)
#             elif ghgh == 2:
#                 guess[0] = b
#                 guess[1] = a
#                 guess[2] = c
#                 print(guess)
#             elif ghgh == 3:
#                 guess[0] = b
#                 guess[1] = c
#                 guess[2] = a
#                 print(guess)
#             elif ghgh == 4:
#                 guess[0] = c
#                 guess[1] = a
#                 guess[2] = b
#                 print(guess)
#             elif ghgh == 5:
#                 guess[0] = c
#                 guess[1] = b
#                 guess[2] = a
#                 print(guess)
#             print(q, "회차")
#             print("컴퓨터의 수", numbers)
#             print("컴퓨터가 뽑은수", guess)
#             q = q + 1

#             # 점수판정
#             for i in range(0, 3):
#                 if guess[i] == user_select_numbers[i]:
#                     st_count = st_count + 1
#                 elif guess[i] in user_select_numbers:
#                     ba_count = ba_count + 1
#                 else:
#                     ou_count = ou_count + 1
#             print_count()
#             if st_count == 3:
#                 ghgh = ghgh + 100

#         num_list_len = len(numbers) + 1000

#     if st_count == 3:
#         print("스트~~라잌!! 컴퓨터가 승리 하였습니다.")


# while st_count != 3:
#     computer_attack()
import random
import time


def print_count():
    print("s | " + "🔴 "*st_count + "⚫ "*(3-st_count) + "| " + str(st_count))
    print("b | " + "🔴 "*ba_count + "⚫ "*(3-ba_count) + "| " + str(ba_count))
    print("o | " + "🔴 "*ou_count + "⚫ "*(3-ou_count) + "| " + str(ou_count))


user_select_numbers = [1, 2, 3]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
trash_num_list = []
jd = 1
q = 1
st_count = 0
win = 0
while True:
    st_count = 0
    ba_count = 0
    ou_count = 0

    random.shuffle(numbers)  # 랜덤 숫자뽑기
    com_guess = []
    for i in range(0, 3):
        com_guess.append(numbers[i])

    time.sleep(0.5)
    print("time", jd)
    jd = jd + 1
    print(com_guess, "중복???")

    if com_guess not in trash_num_list:  # 사용 안된 조합
        print(q, "회차~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        q = q + 1
        for i in range(0, 3):  # 점수판정
            if com_guess[i] == user_select_numbers[i]:
                st_count = st_count + 1
            elif com_guess[i] in user_select_numbers:
                ba_count = ba_count + 1
            else:
                ou_count = ou_count + 1
        if ba_count == 3:  # 점수기반 알고리듬
            numbers = com_guess
        elif ou_count == 3:
            x_count = 0
            for i in range(0, 3):
                for j in range(0, len(numbers)):
                    if com_guess[i] == numbers[j]:
                        numbers[j] = "x"
                        x_count = x_count + 1
            for i in range(0, x_count):
                numbers.remove("x")
        elif st_count == 1:
            if ba_count == 2:
                numbers = com_guess
        trash_num_list.append(com_guess)  # 사용한 수 버림
        print("남은수", numbers)  # 남은수
        print("뽑은수", com_guess)  # 컴퓨터가 뽑은수
        print("쓰레기통", trash_num_list)  # 쓰레기통
        print_count()  # 점수판
        if st_count == 3:  # 경기종료 멘트
            print("경기를 종료합니다.")
            quit()
    else:
        pass
