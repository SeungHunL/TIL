t = int(input())
GNS = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
cnt = [0] * 10
for _ in range(t):

    tc, n = input().split()
    temp = input().split()
    for i in range(int(n)):
        for j in range(10):
            if temp[i] == GNS[j]:
                cnt[j] += 1
                break
    ans = ''
    for i in range(10):
        s=GNS[i]
        ans += f'{s} ' * cnt[i]
    print(cnt)
    print(tc)
