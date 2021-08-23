def Coefficient(length, size):
    if size<length:
        return length
    n = 1
    while 1:
        if length ** n > size:
            break
        n += 1
    n -= 2
    for i in range(length):
        if i * length ** n > size:
            break
    n+=1
    return i,n


sentence, N = input().split()
K = len(sentence)
N = int(N)
i,n =Coefficient(K,N)
Coefficient_list=[]
Coefficient_list.append(i)
N -= i*K**n