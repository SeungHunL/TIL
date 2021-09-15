for _ in range(int(input())):
    A=input()
    stack = ''
    col = []
    for i in range(len(A)):
        if i< len(A)-1 and A[i]!=A[i+1]:
            stack+= A[i]
        else:
            stack+= A[i]
            col.append(stack)
            stack=''
    print(col)
    print(f'#{_+1} {len(col)}')