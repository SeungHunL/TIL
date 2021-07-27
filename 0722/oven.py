A, B = input().split( )
A, B = int(A), int(B)
C = input()
C = int(C)
B = B + C
while B >= 60:
    B -= 60
    A += 1 
if A >= 24:
    A -= 24
print(f'{A} {B}')