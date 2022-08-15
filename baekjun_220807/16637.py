import sys

input = sys.stdin.readline


def cal(me):
    a = int(me[0])
    b = c = 0
    i = 1
    while i < leng+1:
        if me[i] == "+":
            i += 1
            if b:
                if c == 1:
                    a += b
                else:
                    a *= b
                    c = 1
            else:
                c = 1
            b = int(me[i])
        elif me[i] == "*":
            i += 1
            if b:
                b *= int(me[i])
            else:
                b = int(me[i])
                c = 2
        elif me[i] == "-":
            i += 1
            if b:
                if c == 1:
                    a += b
                else:
                    a *= b
                    c = 1
            else:
                c = 1
            b = -1 * int(me[i])
        i += 1
    if c==1:
        a+=b
    else:
        a*=b
    print(a)


leng = int(input())
line = input()
cal(line)
