A = int(input())
while A > 1:
    for i in range(2,A+1):
        if A % i == 0:
            A = A//i
            print(i)
            break
