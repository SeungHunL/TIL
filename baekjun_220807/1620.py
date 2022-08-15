import sys

input = sys.stdin.readline

N, M = map(int, input().split())
deck = []
for i in range(N):
    deck.append(input().strip())
for i in range(M):
    word = input().strip()
    if word.isdigit():
        print(deck[int(word)-1])
    else:
        print(deck.index(word)+1)
