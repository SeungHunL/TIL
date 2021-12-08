line=int(input())
for i in range(line):
    A, B = map(int, input().split())
    C = A+B
    print(f'Case #{i+1}: {C}')
