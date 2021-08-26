import copy


def rcp(arr, v1, v2):
    return v1 if arr[v1] - arr[v2] in (0, 1, -2) else v2


def quick(arr, v):
    if len(v) <= 4:
        return final(arr, v)
    pivot = (v[0] + v[-1]) // 2
    less, more = list(range(v[0], pivot+1)), list(range(pivot+1, v[-1]+1))
    return rcp(arr, quick(arr, less), quick(arr, more))


def final(arr, v):
    stack = v
    stack2 = []
    while 1:
        stack2.append(rcp(arr, stack.pop(0), stack.pop(0)))
        if len(stack) == 0 and len(stack2) == 1:
            return stack2[0]
        elif len(stack) <= 1:
            if stack:
                stack2.append(stack.pop())
            stack = copy.deepcopy(stack2)
            stack2 = []


for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    S_idx = []
    for i in range(N):
        S_idx.append(i)
    print(f'#{_ + 1} {quick(S,S_idx) + 1}')
