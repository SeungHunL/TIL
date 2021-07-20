ST = int(input())
lin = ''
for i in range(1,ST+2):
    for j in range(1,i):
        lin += str(j) + ' '
    print(lin)
    lin = ''
