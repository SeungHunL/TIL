def calculator(arr):
    stack = []
    ans = []
    for i in arr:
        if i in ('+', '-'):
            if stack and stack[-1] in ('*', '/'):
                while stack:
                    ans.append(stack.pop())
            elif stack and stack[-1] in ('+', '-'):
                ans.append(stack.pop())
            stack.append(i)
        elif i in ('*', '/'):
            stack.append(i)
        else:
            ans.append(i)
    while stack:
        ans.append(stack.pop())
    return ans


def equation(arr):
    stack = []
    for i in arr:
        if i == '+':
            stack.append(stack.pop() + stack.pop())
        elif i == '*':
            stack.append(stack.pop() * stack.pop())
        elif i == '-':
            stack.append(stack.pop(-2) - stack.pop())
        elif i == '/':
            stack.append(stack.pop(-2) / stack.pop())
        else:
            stack.append(int(i))
    return stack[0]


for _ in range(10):
    N = int(input())
    num_list = input()
    print(f'#{_ + 1} {equation(calculator(num_list))}')
