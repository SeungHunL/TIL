import sys

input = sys.stdin.readline
X, Y, D, T = map(int, input().split())
l = round((X ** 2 + Y ** 2) ** 0.5, 10)
ans = 1000000000
T = float(T)
if D*2>=l:
    ans=min(T*2,l,T+abs(D-l))
else:
    ans=min(l//D*T+l-l//D*D,
            (l//D+2)*T,
            l,
            (l//D+1)*T+abs((l//D+1)*D-l))
    if T*2<(l-(l//D-1)*T):
        ans= min(ans,(l//D-1+2)*T)
print(ans)
