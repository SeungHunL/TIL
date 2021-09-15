A = '삼성청년소프트웨어아카데미'

B = A[::-1]


C = ''
for i in range(len(A)):
    C += A[len(A)-1-i]

print("".join(list(reversed(A))))
print("".join(reversed(A)))

