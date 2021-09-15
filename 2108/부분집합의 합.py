def part_sum(arr, D):
    n = len(arr)
    for i in range(1 << n):
        count = 0
        for j in range(n + 1):
            if i & (1 << j):
                count += arr[j]
            if count == D:
                return 1
    else:
        return 0


for _ in range(int(input())):
    N, k = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(f'#{_+1} {part_sum(A)}')
