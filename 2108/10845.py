import sys

stack = []

ss = dict(
    push=lambda x: stack.append(x),
    pop=lambda: stack.pop(0) if stack else -1,
    size=lambda: len(stack),
    empty=lambda: 0 if stack else 1,
    front=lambda: stack[0] if stack else -1,
    back=lambda: stack[-1] if stack else -1,
)

for _ in range(int(sys.stdin.readline())):
    data = sys.stdin.readline().split()
    if data[0] == 'push':
        ss['push'](data[1])
    else:
        print(ss[data[0]]())
