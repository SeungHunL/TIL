import sys
import time
start = time.time()
input = sys.stdin.readline

N, M = map(int, input().split())
str1 = {}
for _ in range(N):
    test_str = input().strip()
    n=len(test_str)
    if (test_str[0], n) in str1:
        str1[(test_str[0], n)] = [test_str]+ str1[(test_str[0], n)]
    else:
        str1[(test_str[0], n)] = [test_str]
cnt = 0
for _ in range(M):
    test = input().strip()
    t=len(test)
    k = 0
    if (test[k],t) in str1:
        for i in str1[(test[0],t)]:
            k = 1
            while test[k] == i[k]:
                if k == t-1:
                    cnt += 1
                    break
                k += 1
print(cnt)
print(time.time()-start)

class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children  = {}

class Trie:
    def __init__(self):
        self.head = Node(None)