import sys
input=sys.stdin.readline

words=[0]*40
for i in range(int(input())):
    word=input().strip()
    l=len(word)
    for i in range(l):
        words[ord(word[i])-65]+=10**(l-i-1)

ans=0
for j in range(9,0,-1):
    if not max(words):
        break
    mi=words.index(max(words))
    ans += words[mi] * j
    words[mi]=0
print(ans)