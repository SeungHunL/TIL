import sys

for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline().strip()
    i = 0
    while i<len(N)-1:
        if N[i:i + 2] == '01':
            print('01')
            i += 2
        elif N[i:i + 2] == '10':
            if N[i+2] =='0':

                print('100')
            else:
                print('NO')
                break

        else:
            print('11,00')
            print('NO')
            break
