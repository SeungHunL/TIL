while 1:
    A,B = map(int,input().split())
    if  A > B:
        print('Yes')
    elif A==B==0:
        break
    else:
        print('No')