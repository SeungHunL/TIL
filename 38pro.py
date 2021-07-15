a=[1,2,3,4,3,2,1]
b=str(input())
i=0
while i<=(len(a)-1):
    j=i+1
    while j<=(len(a)-1):
        if a[i]==a[j]:
            del a[j]
        j+=1
    i+=1
print (a)