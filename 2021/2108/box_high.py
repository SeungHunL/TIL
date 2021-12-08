A= [7,4,2,0,0,6,0,7]
high=0
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        if (A[i]>=A[j])and(j-i>high):
            high=j-i
print(high)