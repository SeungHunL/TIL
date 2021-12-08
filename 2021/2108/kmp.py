# tc = input()
pattern = 'ABAABAB'

pi = []
for n in range(len(pattern)):
    cnt = 0
    for i in range(len(pattern) // 2):
        print(i)
        print(pattern[i],pattern[-1-i])
        # if pattern[i] == pattern[n:0:-1][i]:
        #     cnt += 1
        # else:
        #     break
    pi.append(cnt)
print(pi)
