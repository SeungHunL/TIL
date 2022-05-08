import sys
input = sys.stdin.readline

string_1 = input().rstrip()
string_2 = input().rstrip()
max_len = 0
for i in range(len(string_1)):
    for j in range(len(string_2)):
        idx_1 = i
        idx_2 = j
        if string_1[idx_1] == string_2[idx_2]:
            str_len=0
            while idx_1 < len(string_1) and idx_2 < len(string_2) and string_1[idx_1] == string_2[idx_2]:
                idx_1+=1
                idx_2+=1
                str_len+=1
            if str_len>max_len:
                max_len=str_len
print(max_len)
