input='0000000111100000011000000111100110000110000111100111100111111001100111'

def btod(string):
    for i in range(len(string)//7):
        print(int(string[7*i:7*i+7],2),end=' ')

btod(input)