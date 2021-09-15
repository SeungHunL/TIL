lad=[0]
lad[0]=[1,0,1,0,0,1,0,1,0,1]
y=x=0
if lad[y][x] == 1:
    print('xxx')
    for i in range(200):
        if (lad[y][x] == 2) or (y == 99):
            break
        elif x != 99 and (lad[y][x + 1] == 1):
            x += 1
        elif x != 0 and (lad[y][x - 1] == 1):
            x -= 1
        elif lad[y + 1][x] == 1:
            y += 1
        else:
            break
    print('xxx')