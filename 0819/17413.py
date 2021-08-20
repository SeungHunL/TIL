A = input()
count = [0] * len(A)
ans = ''
reverse = ''

s = 0
for i in range(len(A)):
    if A[i] == '<':
        s = 1
        sidx = i
        ans += reverse[::-1]
        reverse = ''
    elif A[i] == '>':
        ans += A[sidx:i + 1]
        s = 0
        sidx = 0
    elif s == 0 and A[i] == ' ':
        ans += reverse[::-1] + ' '
        reverse = ''
    elif i == len(A) - 1:
        reverse += A[i]
        ans += reverse[::-1]
    elif s == 0:
        reverse += A[i]
print(ans)

