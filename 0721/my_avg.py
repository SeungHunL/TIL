def my_avg(*tup):
    sum = 0 
    count = 0
    for i in range(len(tup)):
        sum += tup[i]
        count += 1
    return sum/count
result = my_avg(77, 83, 95, 80, 70 )
print(result)

        
    