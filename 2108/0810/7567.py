i = input()
s=0
for n in range(0,len(i)):
    if n == 0:
        s = 10
    elif i[n]=='(' and i[n-1]=='(':
        s += 5
    elif i[n]==')'and i[n-1]=='(':
        s+=10
    elif i[n]=='(' and i[n-1]==')':
        s+=10
    else:
        s+=5
print(s)