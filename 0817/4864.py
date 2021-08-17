T = int(input())
for _ in range(T):
    A = input()
    B = input()
    for i in range(len(B)):
        if B[i] == A[-1]:
            for j in range(1, len(A)):
                if A[-j-1] != B[i - j]:
                    break
            else:
                print(f'#{_ + 1} 1')
                break
    else:
        print(f'#{_ + 1} 0')
