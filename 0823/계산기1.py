def plus(arr):
    stack = []
    ans = []
    for i in arr:
        if i == '+':
            stack.append(i)
        else:
            if stack:
                ans.append(i)
                ans.append(stack.pop())
            else:
                ans.append(i)
    return ans


def equation(arr):
    stack = []
    s = 0
    for i in arr:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        else:
            stack.append(int(i))
    return stack[0]


for _ in range(10):
    N = int(input())
    num_list = input()
    print(equation(plus(num_list)))
