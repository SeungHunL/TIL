while 1:
    A, B = map(int,input().split())
    if A==B==0:
        break
    if A % B == 0:
        print('multiple')
    elif B % A == 0:
        print('factor')
    else:
        print('neither')
