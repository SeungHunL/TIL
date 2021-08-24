for _ in range(int(input())):
    form = input().split()
    stack = []
    for i in form:
        if len(stack) >= 2 and i in ('+', '-', '*', '/'):
            if i == '+':
                stack.append(stack.pop(-2) + stack.pop())
            elif i == '-':
                stack.append(stack.pop(-2) - stack.pop())
            elif i == '*':
                stack.append(stack.pop(-2) * stack.pop())
            elif i == '/':
                stack.append(stack.pop(-2) / stack.pop())
        elif i == '.':
            ans = 1
            continue
        else:
            if i in ('+', '-', '*', '/'):
                ans = 0
                break
            stack.append(int(i))
    print(f'#{_ + 1} {int(stack.pop())}') if ans and len(stack) == 1 else print(f'#{_ + 1} error')
