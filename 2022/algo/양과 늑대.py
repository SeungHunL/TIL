class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def solution(info, edges):
    global lamb, wolf, node_list, max_lamb, route
    def recursion(num):
        global lamb, wolf, node_list, max_lamb, route
        route.append(num)
        node_list=[]
        for i in route:
            m = mem[i]
            ml,mr = m.left, m.right
            if ml :
                if ml.data not in route:
                    node_list.append(ml.data)
                if mr and mr.data not in route:
                    node_list.append(mr.data)
        # print(route,node_list)
        # print(lamb,wolf)
        for i in node_list:
            if not info[i]:
                if i not in route:
                    lamb += 1
                    if lamb > max_lamb:
                        max_lamb = lamb
                    recursion(i)
                    lamb -= 1
            elif info[i] and lamb > wolf + 1:
                if i not in route:
                    wolf += 1
                    recursion(i)
                    wolf -= 1
        route.pop()

    mem = []
    for i in range(len(info) + 1):
        mem.append(Node(i))
    for i in edges:
        if mem[i[0]].left:
            mem[i[0]].right = mem[i[1]]
        else:
            mem[i[0]].left = mem[i[1]]

    lamb, wolf = 1, 0
    max_lamb=1
    route=[]
    recursion(0)
    return max_lamb

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info,edges))