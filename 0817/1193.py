N = int(input())
i = 0
s = 0
while N > s :
    i += 1
    s += i
if i % 2 :
    x = i - (N - (s - i)) + 1
    y = N - (s - i)
else:
    x = N - (s - i)
    y = i - (N - (s - i))+1
print(f'{x}/{y}')
