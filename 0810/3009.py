def dg(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
if dg(A, B) >= dg(B, C) and dg(A, B) >= dg(A, C):
    A[0] = A[0] + B[0] - C[0]
    A[1] = A[1] + B[1] - C[1]
elif dg(B, C) >= dg(A, B) and dg(B, C) >= dg(A, C):
    A[0] = C[0] + B[0] - A[0]
    A[1] = C[1] + B[1] - A[1]
else:
    A[0] = A[0] + C[0] - B[0]
    A[1] = A[1] + C[1] - B[1]
print(f'{A[0]} {A[1]}')
