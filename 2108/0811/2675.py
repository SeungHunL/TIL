T = int(input())
for num in range(T):
    N, alpha = input().split()
    beta=''
    for i in range(0,len(alpha)):
        for j in range(int(N)):
            beta += alpha[i]
    print(beta)