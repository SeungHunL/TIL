for _ in range(int(input())):
    A, B = input().split()
    c = 0
    tenet = []
    for i in range(len(A)-len(B)+1):
        if A[i] == B[0] and (i not in tenet):
            for j in range(1, len(B)):
                if B[j] != A[i + j]:
                    break
            else:
                for s in range(len(B)):
                    tenet.append(i+s)
                c += 1

    print(f'#{_ + 1} {len(A) - c * (len(B) - 1)}')
