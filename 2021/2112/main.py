import random

DEER = 0
RABBIT = 1
SNAKE = 2

# 아래 Me 함수를 작성해서 제출하세요.
buulgyeong2_2_list=[]
def Me(opp, turn, opp_prev, opp_last_pattern):
    olp=opp_last_pattern
    global buulgyeong2_2_list
    if len(buulgyeong2_2_list)==10:
        buulgyeong2_2_list = []
    elif len(buulgyeong2_2_list)>=3:
        if buulgyeong2_2_list[-1]==buulgyeong2_2_list[-2]==buulgyeong2_2_list[-3]:
            if buulgyeong2_2_list[-1]==2:
                buulgyeong2_2_list.append(0)
                return 0

    # 첫번째 턴
    if turn==0:
        if opp_last_pattern[0][0] == -1:
            buulgyeong2_2_list.append(0)
            return 0
        else:
            # 상대가 이전게임에서 첫 턴에 사슴을 내면 우리도 사슴을 낸다.
            if opp_last_pattern[0][0]==0:
                buulgyeong2_2_list.append(0)
                return 0
            # 아닐 땐 뱀
            else:
                buulgyeong2_2_list.append(2)
                return 2
    # 2번째 턴 이후
    # 상대가 규칙이 있는지 세는 2차원 행렬
    animal=[[0]*3 for _ in range(3)]
    for i in range(9):
        animal[olp[0][i]][olp[0][i + 1]] += 1
    # 규칙이 있을 때
    # 상대가 0뒤에 무조건 0이 올 때:
    if animal[opp_prev][0] and not animal[opp_prev][1] and not animal[opp_prev][2]:
        buulgyeong2_2_list.append(0)
        return 0
    elif animal[opp_prev][1] and not animal[opp_prev][0] and not animal[opp_prev][2]:
        buulgyeong2_2_list.append(2)
        return 2
    elif animal[opp_prev][2] and not animal[opp_prev][0] and not animal[opp_prev][1]:
        buulgyeong2_2_list.append(2)
        return 2
    # 규칙이 없을 때
    # 상대도 우리처럼 상대의 이전 데이터들로 전략을 구성할 때:
    buulgyeong2_2_list.append(0)
    return 0

def Opponent1(opp, turn, opp_prev, opp_last_pattern):
    if opp_prev == 2: return 2
    return 0

def Opponent2(opp, turn, opp_prev, opp_last_pattern):
    if opp_last_pattern.count([2, 2, 1, 2, 2, 1, 2, 2, 1, 2]) >= 7:
        if turn == 0 or turn == 3 or turn == 6:
            return 0
        else:
            return 2
    if turn == 2 or turn == 5 or turn == 8:
        return 0
    return 2

def Opponent3(opp, turn, opp_prev, opp_last_pattern):
    global buulgyeong2_1_snake_cnt
    if turn == 0:
        buulgyeong2_1_snake_cnt = 0
    # 이번판에 상대방이 낸 패턴 기록
    if turn > 0:
        buulgyeong2_1_cur_pattern[turn - 1] = opp_prev
    idx = -1
    for i in range(len(opp_last_pattern)):
        if sum(opp_last_pattern[i]) == -10:
            break
        idx = i
    my_result = 2
    is_same = True
    is_copy = True

    for t in range(turn):
        if opp_last_pattern[idx][t] != buulgyeong2_1_cur_pattern[t]:
            is_same = False
        if t > 1 and buulgyeong2_1_my_pattern[t - 1] != buulgyeong2_1_cur_pattern[t]:
            is_copy = False

    if turn < 3:
        buulgyeong2_1_snake_cnt += 1
        my_result = 2
    else:
        if idx > -1:
            if is_same:
                if opp_last_pattern[idx][turn] == 0:
                    buulgyeong2_1_snake_cnt = 0
                    my_result = 1
                elif opp_last_pattern[idx][turn] == 1:
                    buulgyeong2_1_snake_cnt += 1
                    my_result = 2
                else:
                    if buulgyeong2_1_snake_cnt > 3:
                        buulgyeong2_1_snake_cnt = 0
                        my_result = 0
                    else:
                        buulgyeong2_1_snake_cnt += 1
                        my_result = 2
            else:
                if is_copy:
                    if buulgyeong2_1_my_pattern[turn - 1] == 0:
                        buulgyeong2_1_snake_cnt = 0
                        my_result = 1
                    elif buulgyeong2_1_my_pattern[turn - 1] == 1:
                        buulgyeong2_1_snake_cnt += 1
                        my_result = 2
                    else:
                        if buulgyeong2_1_snake_cnt > 3:
                            buulgyeong2_1_snake_cnt = 0
                            my_result = 0
                        else:
                            buulgyeong2_1_snake_cnt += 1
                            my_result = 2
                else:
                    if buulgyeong2_1_my_pattern[turn - 1] == 0:
                        buulgyeong2_1_snake_cnt += 1
                        my_result = 2
                    elif buulgyeong2_1_my_pattern[turn - 1] == 1:
                        if buulgyeong2_1_snake_cnt > 3:
                            buulgyeong2_1_snake_cnt = 0
                            my_result = 0
                        else:
                            buulgyeong2_1_snake_cnt += 1
                            my_result = 2
                    else:
                        if buulgyeong2_1_snake_cnt > 3:
                            buulgyeong2_1_snake_cnt = 0
                            my_result = 0
                        else:
                            buulgyeong2_1_snake_cnt += 1
                            my_result = 2
        else:
            if is_copy:
                if buulgyeong2_1_my_pattern[turn - 1] == 0:
                    buulgyeong2_1_snake_cnt = 0
                    my_result = 1
                elif buulgyeong2_1_my_pattern[turn - 1] == 1:
                    buulgyeong2_1_snake_cnt += 1
                    my_result = 2
                else:
                    if buulgyeong2_1_snake_cnt > 3:
                        buulgyeong2_1_snake_cnt = 0
                        my_result = 0
                    else:
                        buulgyeong2_1_snake_cnt += 1
                        my_result = 2
            else:
                if buulgyeong2_1_my_pattern[turn - 1] == 0:
                    buulgyeong2_1_snake_cnt += 1
                    my_result = 2
                elif buulgyeong2_1_my_pattern[turn - 1] == 1:
                    if buulgyeong2_1_snake_cnt > 3:
                        buulgyeong2_1_snake_cnt = 0
                        my_result = 0
                    else:
                        buulgyeong2_1_snake_cnt += 1
                        my_result = 2
                else:
                    if buulgyeong2_1_snake_cnt > 3:
                        buulgyeong2_1_snake_cnt = 0
                        my_result = 0
                    else:
                        buulgyeong2_1_snake_cnt += 1
                        my_result = 2
    buulgyeong2_1_my_pattern[turn] = my_result

    return my_result


# 전역변수
buulgyeong2_1_cur_pattern = [-1] * 10
buulgyeong2_1_my_pattern = [-1] * 10
buulgyeong2_1_snake_cnt = 0

def Register(name, func):
    global  f_inx
    names[f_inx] = name
    f[f_inx] = func
    f_inx += 1


###################  main  #######################
f = [0] * 150
names = [""] * 100
f_inx = 0
total_score =[0] * 150
last_pattern = [[[0] * 10 for _ in range(150)] for _ in range(150)] # [팀][대전][패턴]
pattern_count = [0] * 150

Register("Me", "Me")

Register("Opp1", "Opponent1")
Register("Opp2", "Opponent2")
Register("Opp3", "Opponent3")

for i in range(140):
    for j in range(140):
        for k in range(10):
            last_pattern[i][j][k] = -1

for i in range(1, f_inx):
    for j in range(f_inx):
        team_a = j % f_inx
        team_b = (j+i) % f_inx
        print("[{}] vs [{}]".format(names[team_a], names[team_b]))

        a_game_score = 0
        b_game_score = 0

        prev_a = -1
        prev_b = -1

        team_a_cont = 0
        team_b_cont = 0

        a_pattern = [0] * 10
        b_pattern = [0] * 10

        for k in range(10):
            print("<turn {}>".format(k))
            a = eval("{}(team_a, k, prev_b, last_pattern[team_b])".format(f[team_a]))
            b = eval("{}(team_b, k, prev_a, last_pattern[team_a])".format(f[team_b]))
            a_pattern[k] = a
            b_pattern[k] = b

            if a == prev_a: team_a_cont += a+1
            else: team_a_cont = 0
            if b == prev_b: team_b_cont += b+1
            else: team_b_cont = 0

            if a != 0 and a != 1 and a != 2: team_a_cont = 100
            if b != 0 and b != 1 and b != 2: team_b_cont = 100

            prev_a = a
            prev_b = b

            a_score = 0
            b_score = 0

            if a == DEER and b == DEER: a_score = 50; b_score = 50;
            elif a == DEER and b == RABBIT: a_score = 0; b_score = 20;
            elif a == DEER and b == SNAKE: a_score = 0; b_score = 10;
            elif a == RABBIT and b == DEER: a_score = 20; b_score = 0;
            elif a == RABBIT and b == RABBIT: a_score = 20; b_score = 20;
            elif a == RABBIT and b == SNAKE: a_score = 0; b_score = 30;
            elif a == SNAKE and b == DEER: a_score = 10; b_score = 0;
            elif a == SNAKE and b == RABBIT: a_score = 30; b_score = 0;
            elif a == SNAKE and b == SNAKE: a_score = 10; b_score = 10;

            a_score -= team_a_cont
            b_score -= team_b_cont
            a_score += random.randrange(3)
            b_score += random.randrange(3)

            a_game_score += a_score
            b_game_score += b_score


            if a == 0: print(f"[{names[team_a]}] : DEER, ",  end="")
            elif a == 1: print(f"[{names[team_a]}] : RABBIT, ", end="")
            elif a == 2: print(f"[{names[team_a]}] : SNAKE, ", end="")

            if b == 0: print(f"[{names[team_b]}] : DEER")
            elif b == 1: print(f"[{names[team_b]}] : RABBIT")
            elif b == 2: print(f"[{names[team_b]}] : SNAKE")

            print(f"[{names[team_a]}] score: This turn:{a_score}, Game score:{a_game_score}, Total score:{total_score[team_a] + a_game_score}")
            print(f"[{names[team_b]}] score: This turn:{b_score}, Game score:{b_game_score}, Total score:{total_score[team_b] + b_game_score}")

        for z in range(10):
            last_pattern[team_a][pattern_count[team_a]][z] = a_pattern[z]
            last_pattern[team_b][pattern_count[team_b]][z] = b_pattern[z]
        pattern_count[team_a] += 1
        pattern_count[team_b] += 1

        print("<game result>")
        if a_game_score == b_game_score: print("Draw")
        else:
            print("Win : [{}]".format(names[team_a] if a_game_score > b_game_score else names[team_b]))
        print()
        total_score[team_a] += a_game_score
        total_score[team_b] += b_game_score

print("<Final score>")
max_inx = 0
max_score = 0
for i in range(f_inx):
    print(f"[{names[i]}] Total Score : {total_score[i]}")
    if max_score < total_score[i]:
        max_inx = i
        max_score = total_score[i]

print(f"<Winner : [{names[max_inx]}] !!!>")


