for _ in range(10):
    N=int(input())
    T= input()
    duet = []
    for i in T:
        if i in ('(','[','{','<'):
            duet.append(i)
        elif i in (')',']','}','>'):
            if len(duet) == 0:
                print(f'#{_+1} 0')
                break
            elif duet[-1]=='(' and i==')':
                duet.pop()
            elif duet[-1]=='<' and i=='>':
                duet.pop()
            elif duet[-1]=='{' and i=='}':
                duet.pop()
            elif duet[-1]=='[' and i==']':
                duet.pop()
            else:
                print(f'#{_+1} 0')
                break
    else:
        if len(duet)==0:
            print(f'#{_+1} 1')
        else:
            print(f'#{_+1} 0')