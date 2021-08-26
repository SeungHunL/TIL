
for _ in range(1):
    T = int(input())
    N = [0] * 100
    A = [''] * 100
    for t in range(100):
        N[t] = list(map(int, input().split()))
    for i in range(100):
        for j in range(100):
            A[i]+=str(N[j][i])
        A[i] = A[i].replace("0", "")
    print(A)
    count = 0
    for k in range(100):
        for l in range(1,len(A[k])):
            if A[k][l] == '2' and A[k][l-1] == '1':
                count += 1
    print(count)
