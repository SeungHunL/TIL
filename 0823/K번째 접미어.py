def soltcaramel(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]


for _ in range(int(input())):
    N = int(input())
    word = input()
    l = len(word)
    word_list = []
    for i in range(l):
        word_list.append(word[i:])
    soltcaramel(word_list)

    if N <= l:
        print(f'#{_ + 1} {word_list[N - 1]}')
    else:
        print('none')
