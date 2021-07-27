def dict_list_sum(diclst):
    dicsum =0
    for i in range(0,len(diclst)):
        dicsum += diclst[i]['age']
    return dicsum
dict_list_sum([{'name': 'kim', 'age': 12},
               {'name': 'lee', 'age': 4}])
