s = 0
for i in range(5):
    t = int(input())
    if t<40:
        t=40
    s+=t
print(int(s/5))