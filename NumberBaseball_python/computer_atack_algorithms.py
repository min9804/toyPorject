import random


def print_count():
    print("s | " + "🔴 "*st_count + "⚫ "*(3-st_count) + "| " + str(st_count))
    print("b | " + "🔴 "*ba_count + "⚫ "*(3-ba_count) + "| " + str(ba_count))
    print("o | " + "🔴 "*ou_count + "⚫ "*(3-ou_count) + "| " + str(ou_count))


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
user_select_numbers = [5, 3, 2]

line_up_list = []  # 숫자 조합 만들기
num = 122
for i in range(123, 988):
    num = num + 1
    str_num = str(num)
    if str_num[0] != str_num[1]:
        if str_num[1] != str_num[2]:
            if str_num[2] != str_num[0]:
                a = int(str_num[0])
                b = int(str_num[1])
                c = int(str_num[2])
                line_up = []
                line_up.append(a)
                line_up.append(b)
                line_up.append(c)
                line_up_list.append(line_up)
print(line_up_list)

###############################################
q = 1
while True:
    print(q, "회차")
    random.shuffle(line_up_list)
    com_guess = line_up_list[0]  # 숫자 선정(랜덤)
    print(com_guess)
    line_up_list.remove(com_guess)  # 선정 숫자 제거

    st_count = 0
    ba_count = 0
    ou_count = 0
    for i in range(0, 3):  # 점수판정
        if com_guess[i] == user_select_numbers[i]:
            st_count = st_count + 1
        elif com_guess[i] in user_select_numbers:
            ba_count = ba_count + 1
        else:
            ou_count = ou_count + 1
    print_count()  # 점수표시
    score = []
    score.append(st_count)
    score.append(ba_count)
    score.append(ou_count)

    x_count = 0
    for j in range(0, len(line_up_list)):  # 점수기반 라인업 제거
        jd_st_count = 0
        jd_ba_count = 0
        jd_ou_count = 0
        jd_guess = line_up_list[j]
        for k in range(0, 3):  # 점수판정
            if jd_guess[k] == com_guess[k]:
                jd_st_count = jd_st_count + 1
            elif jd_guess[k] in com_guess:
                jd_ba_count = jd_ba_count + 1
            else:
                jd_ou_count = jd_ou_count + 1

        jd_score = []
        jd_score.append(jd_st_count)
        jd_score.append(jd_ba_count)
        jd_score.append(jd_ou_count)

        if score != jd_score:
            line_up_list[j] = "x"
            x_count = x_count + 1

    for x in range(0, x_count):  # 생성된 "x" 제거
        line_up_list.remove("x")
    print(line_up_list)

    q = q + 1

    if st_count == 3:
        print("게임을 종료 합니다.")
        quit()
