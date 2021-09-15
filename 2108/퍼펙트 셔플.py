for _ in range(int(input())):
    N = int(input())
    deck = input().split()
    front = deck[:(len(deck)+1) // 2]
    back = deck[(len(deck)+1) // 2:]
    print(front,back)
    ans = ''
    for i in range(len(front)):
        ans += front.pop(0) + ' '
        if back: ans += back.pop(0) + ' '
    print(f'#{_ + 1} {ans}')
