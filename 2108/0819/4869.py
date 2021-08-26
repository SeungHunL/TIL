def jax(x):
    if x == 1:
        return 1
    else:
        return x * jax(x - 1)


for _ in range(int(input())):
    N = int(input())
    ans = 0
    k = N // 10
    for i in range(k + 1):
        s = 0
        for j in range(k + 1):
            if i + 2 * j == k:
                if j and i:
                    s = (jax(i + j) / (jax(i) * jax(j))) * (2 ** j)
                elif i == 0:
                    s = 2**j
                else:
                    s = 1
                ans += s

    print(f'#{_ + 1} {int(ans)}')
