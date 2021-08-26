def all_list_sum(lst):
    lstsum = 0
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lstsum += lst[i][j]
    return lstsum
all_list_sum([[1],[2,3],[4,5,6],[7, 8, 9, 10]])

