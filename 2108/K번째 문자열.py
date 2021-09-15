def soltcaramel(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]


for _ in range(int(input())):
    N = int(input())
    words = input()
    l = len(words)
    word_list = []
    for i in range(l):
        for j in range(i + 1, l + 1):
            word_list.append(words[i:j])
    word_list=list(set(word_list))
    soltcaramel(word_list)
    if len(word_list) >= N:
        print(f'#{_ + 1} {word_list[N - 1]}')
    else:
        print(f'#{_ + 1} none')
