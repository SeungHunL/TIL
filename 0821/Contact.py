import sys

for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline().strip()
    i = 0
    while 1:
        if N[i:i + 2] == '01':
            print('01')
            i += 2
        elif N[i:i + 2] == '01':
            i+= 3
            print('100')
            while N[i] != '1':
                i += 1
            i += + 1
            print(i,N[i])
        else:
            print('10,11,101')
            print('NO')
            break
