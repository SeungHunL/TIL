T = int(input())
for _ in range(T):
    S = input()
    count = 0
    piece = 0
    for n in range(len(S)-1):
        if S[n] == '(':
            if S[n + 1] == '(':
                count += 1
            else:
                piece += count
        else:
            if S[n + 1] == '(':
                pass
            else:
                piece += 1
                count -= 1

    print(f'#{_+1} {piece}')
