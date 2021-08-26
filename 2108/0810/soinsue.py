N = int(input())
lis = [2, 3, 5, 7, 11]
cnt = [0] * 12
while N > 1:
    for i in lis:
        if N % i == 0:
            N = N // i
            lis.append(i)
            break
for j in lis:
    cnt[j] += 1
print(f'#{1} {cnt[2]} {cnt[3]} {cnt[5]} {cnt[7]} {cnt[11]}')