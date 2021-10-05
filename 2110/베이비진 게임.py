def win(arr):
    for i in range(3,7):
        if runs(arr[:i]):
            return i
        if tri(arr[:i]):
            return i
    return 7
def runs(arr):
    arr.sort()
    arr=list(set(arr))
    for i in range(len(arr)-2):
        if arr[i]+1==arr[i+1] and arr[i+1]+1==arr[i+2]:
            return 1
def tri(arr):
    for i in range(len(arr)-2):
        if arr.count(arr[i])==3:
            return 1

for q in range(int(input())):
    draw = list(map(int, input().split()))
    A, B = [], []
    for i in range(6):
        A.append(draw[i * 2])
        B.append(draw[i * 2 + 1])
    A = win(A)
    B = win(B)
    if A == B and A==7 :
        print(f'#{q + 1} 0')
    elif A <= B:
        print(f'#{q + 1} 1')
    else:
        print(f'#{q + 1} 2')
