import sys
import time
start = time.time()
input = sys.stdin.readline


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.data = string

    def search(self, string):
        curr_node = self.head

        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.data:
            return True
        else:
            return False

N, M = map(int, input().split())
str1 = Trie()
for _ in range(N):
    in_str = input().strip()
    str1.insert(in_str)
cnt = 0
for _ in range(M):
    test_str = input().strip()
    if str1.search(test_str):
        cnt+=1

print(cnt)
print(time.time()-start)

