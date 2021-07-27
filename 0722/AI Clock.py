A, B, C = input().split( )
D = input()
A, B = int(A), int(B)
C = int(C) + int(D)
while C >= 60:
    C -= 60
    B += 1
while B >= 60:
    B -= 60
    A += 1                                                                                                                                                                                   
while A >= 24:
    A -= 24
print(A, B, C)