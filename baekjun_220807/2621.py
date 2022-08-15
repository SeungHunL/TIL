import sys

input = sys.stdin.readline

deck={0:[],1:[],3:[],4:[]}
colors=[0]*4
nums= [0]*9
for i in range(5):
    color, num = input().split()
    if color == "R":
        color = 0
    elif color == "B":
        color = 1
    elif color == "Y":
        color = 2
    else:
        color = 3
    colors[color]+=1
    nums[num]+=1
    deck[color].append(num)
if max(colors)==5:
    ans = 900+
elif max(colors)==4:
