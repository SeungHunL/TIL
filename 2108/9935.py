import sys

t = sys.stdin.readline().strip()
b = list(sys.stdin.readline().strip())
stack =[]
for i in range(len(t)):
    if b[-1]!=t[i]:
        stack.append(t[i])
    else:
        stack.append(t[i])
        if stack[-len(b):] == b:
            del stack[-len(b):]

print(''.join(stack)if stack else 'FRULA')


