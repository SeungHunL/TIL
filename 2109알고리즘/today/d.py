import sys

input = sys.stdin.readline


# dfs
def dfs(graph, start, visited):
    visited.append(start)
    print(start)
    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)
    return


n = int(input())
# 이중 딕셔너리
tree = {}
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    if a in tree:
        tree[a].update({b: c})
    else:
        tree[a] = {b: c}
    if b in tree:
        tree[b].update({a: c})
    else:
        tree[b] = {a: c}


# 끝단 찾기
leaf = []
for i in tree:
    if len(tree[i]) == 1:
        leaf.append(i)
for j in tree:
    if len(tree[j]) == 2:

        tree[f][g]=tree[j][f]+tree[j][g]
        tree[g][f]=tree[j][f]+tree[j][g]
        del tree[j]

# 가중치 출력, 비교
mx = 0
for j in range(len(leaf)):
    visited=[]
    dfs(tree,leaf[j],visited)
    print()
