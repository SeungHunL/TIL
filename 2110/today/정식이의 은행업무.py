def tri(n):
    ans = []
    while n:
        ans.append(f'{n % 3}')
        n //= 3
    return ''.join(ans[::-1])


for q in range(int(input())):
    n2 = input()
    n3 = input()
    l2 = []
    for i in range(1, 1 + len(n2)):
        if n2[-i] == '0':
            l2.append(int(n2, 2) + 2 ** (i - 1))
        else:
            l2.append(int(n2, 2) - 2 ** (i - 1))
    for j in l2:
        n23=tri(j)
        flag=0
        if len(n3)==len(n23):
            for i in range(len(n23)):
                if n3[i] != n23[i]:
                    flag +=1
                    if flag==2:
                        break
            else:
                print(f'#{q + 1} {j}')
                break
        elif len(n3)+1==len(n23) or len(n3)==len(n23)+1:
            for i in range(1,len(n23)):
                if n3[i] != n23[i]:
                    break
            else:
                print(f'#{q + 1} {j}')
                break