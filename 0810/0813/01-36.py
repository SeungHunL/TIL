def itta(snum):
    ans = 0
    for i in range(len(snum)):
        if snum[i] == '0':
            num = 0
        elif snum[i] == '1':
            num = 1
        elif snum[i] == '2':
            num = 2
        elif snum[i] == '3':
            num = 3
        elif snum[i] == '4':
            num = 4
        elif snum[i] == '5':
            num = 5
        elif snum[i] == '6':
            num = 6
        elif snum[i] == '7':
            num = 7
        elif snum[i] == '8':
            num = 8
        elif snum[i] == '9':
            num = 9
        ans += num * (10 ** (len(snum)-i-1))
    return ans
def atti(snum):
    ans = ''
    while snum :
        snum % 10
        if snum % 10 == 0:
            num = '0'
        elif snum % 10 == 1:
            num = '1'
        elif snum % 10 == 2:
            num = '2'
        elif snum % 10 == 3:
            num = '3'
        elif snum % 10 == 4:
            num = '4'
        elif snum % 10 == 5:
            num = '5'
        elif snum % 10 == 6:
            num = '6'
        elif snum % 10 == 7:
            num = '7'
        elif snum % 10 == 8:
            num = '8'
        elif snum % 10 == 9:
            num = '9'
        snum //= 10
        ans += num
    return ans[::-1]

print((atti(1234)))
