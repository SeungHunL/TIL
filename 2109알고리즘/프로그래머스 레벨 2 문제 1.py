def solution(n):
    K = 0
    while n:
        if n % 2:
            K += 1
            n -= 1
        n //= 2

    ans = K
    print(ans)
    return ans
solution(5000)