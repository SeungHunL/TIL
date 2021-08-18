code= {
    '000000':'A', #0
    '001111':'B', #15
    '010011':'C', #19
    '011100':'D', #28
    '100110':'E', #38
    '101001':'F', #41
    '110101':'G',
    '111010':'H'
}
////////////////////////////////////////못 품

N= int(input())
T= input()
counting=[0]*8
ans =''

for x in range(N):
    for j in code:
        count = 0
        for i in range(6):
            if j[i]==T[6*x+i]:
                count +=1


print(code['000000'])