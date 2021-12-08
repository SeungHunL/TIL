N = int(input())
divi = ''
count = 0
for i in range(1,N+1):
    if N%i==0:
        divi += str(i) + ' '
print(divi)