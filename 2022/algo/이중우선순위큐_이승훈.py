import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    for command in operations:
        if command[0]=="I":
            heapq.heappush(min_heap, int(command[2:]))
            heapq.heappush(max_heap, -int(command[2:]))
        else:
            if min_heap:
                #최소힙
                if command[2:]=="-1":
                    max_heap.remove(-heapq.heappop(min_heap))
                #최대힙
                else:
                    min_heap.remove(-heapq.heappop(max_heap))
    if min_heap:
        return [-heapq.heappop(max_heap),heapq.heappop(min_heap)]
    else:
        return [0,0]

# import heapq
#
# def solution(operations):
#     heap = []
#     for command in operations:
#         if command[0]=="I":
#             heapq.heappush(heap,int(command[2:]))
#         else:
#             #최소힙
#             if command[2]=="-":
#                 heapq.heappop(heap)
#             #최대힙
#             else:
#                 if heap:
#                     #최대힙
#                     max_heap=[]
#                     for item in heap:
#                         heapq.heappush(max_heap,(-item,item))
#                     max_int=heapq.heappop(max_heap)[1]
#                     heap.remove(max_int)
#     if heap:
#         return [max(heap),min(heap)]
#     else:
#         return [0,0]

print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

print(solution(	["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))