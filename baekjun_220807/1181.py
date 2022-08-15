import sys

input = sys.stdin.readline

N = int(input())
dic = {}
words = []
for i in range(N):
    word = input().strip()
    nw = len(word)
    if nw in dic:
        dic[len(word)].add(word)
    else:
        dic[len(word)] = set([word])
ss = list(dic.keys())
ss.sort()
for i in ss:
    ass = list(dic[i])
    ass.sort()
    for j in ass:
        print(j)
