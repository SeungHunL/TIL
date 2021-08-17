grid = [[0]*100 for _ in range(100)]
count = 0
for __ in range(4):
    A = list(map(int,input().split()))
    for x in range(A[0],A[2]):
        for y in range(A[1],A[3]):
            if not grid[x][y] :
                grid[x][y] = 1
                count += 1
print(count)