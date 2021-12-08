def get_secret_number(name):
    sum = 0
    for i in range(len(name)):
        sum += ord(name[i])
    return sum
print(get_secret_number('tom'))