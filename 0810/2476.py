def dice(A, B, C):
    if A == B and B == C:
        return (10000 + A * 1000)
    elif A == B:
        return (1000 + 100 * A)
    elif B == C:
        return (1000 + 100 * B)
    elif A == C:
        return (1000 + 100 * A)
    elif A > B and A > C:
        return (A * 100)
    elif B > A and B > C:
        return (B * 100)
    else:
        return (C * 100)


T = int(input())
mx = 0
for num in range(T):
    X, Y, Z = map(int, input().split())
    if mx < dice(X, Y, Z):
        mx = dice(X, Y, Z)
print(mx)
