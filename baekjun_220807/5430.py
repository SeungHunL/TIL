import sys

input = sys.stdin.readline

for _ in range(int(input())):
    ff = input().strip()
    n = int(input())
    p=input()
    if n==0:
        nums=[]
    else:
        nums = list(map(int,p.strip()[1:-1].split(',')))

    d=1
    f,b=0,0
    for i in range(len(ff)):
        if ff[i]=="R":
            d*=-1
        else:
            if n>f+b:
                if d>0:
                    f+=1
                else:
                    b+=1
            else:
                print("error")
                break
    else:
        if b==0:
            nums = nums[f:]
        else:
            nums=nums[f:-b]
        if d<0:
            nums=nums[::-1]
        ans=','.join(list(map(str,nums)))
        print(f'[{ans}]')