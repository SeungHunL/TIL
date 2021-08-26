A,B,C = map(int,input().split())
if A==B and B==C:
    print(10000+A*1000)
elif A==B:
    print(1000+100*A)
elif B==C:
    print(1000 + 100*B)
elif A==C:
    print(1000 + 100*A)
elif A>B and A>C:
    print(A*100)
elif B>A and B>C:
    print(B*100)
else:
    print(C*100)
