input='01D06079861D79F99F'

def btod(string):
    htob=''
    for _ in range(len(string)):
        htob+=str(format(int('0x'+string[_],16),'04b'))

    for i in range(len(htob)//7+1):
        print(int(htob[7*i:7*i+7],2),end=' ')

btod(input)
