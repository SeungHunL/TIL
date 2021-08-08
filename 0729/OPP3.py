import random
class ClassHelper:
    def __init__(self,list):
        self.list = list
    def pick(self,n):
        nlst = []
        nlst.append(random.sample(self.list,n))
        return nlst
    def match_pair(self):
        olst = self.list
        nlst = []
        k = len(olst)//2
        for i in range(0,k):
            slst=[]
            if len(olst) ==3 :
                slst = olst
            elif len(olst) >= 2:
                slst.append(olst.pop(random.randint(0,len(olst))))
                slst.append(olst.pop(random.randint(0,len(olst))))
            nlst.append(slst)
        return nlst
ch = ClassHelper(['김싸피', '이싸피', '조싸피', '박싸피', '정싸피'])

print(ch.match_pair())