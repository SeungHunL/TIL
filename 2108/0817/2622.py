N = int(input())
count = 0
for i in range(N // 3, N - 2):
    for j in range((N - i) // 2, i + 1):
        if (j >= N - i - j) and (N - i - j) and N > 2 * i:
            count += 1
print(count)
