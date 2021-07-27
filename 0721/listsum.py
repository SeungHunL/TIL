def list_sum(lst):
    lisum = 0
    for i in range(0,len(lst)):
        lisum += lst[i]
    return (lisum)
list_sum([1, 2, 3, 4, 5])