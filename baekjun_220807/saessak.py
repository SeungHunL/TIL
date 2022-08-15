# import sys
#
# input=sys.stdin.readline
#
# N,X=map(int,input().split())
# nums=list(map(int,input().split()))
# for i in nums:
#     if i<X:
#         print(i, end=" ")

# import sys
#
# input=sys.stdin.readline
#
# while 1:
#     try:
#         a,b=map(int,input().split())
#         print(a+b)
#     except ValueError:
#         break
# import sys
#
# input=sys.stdin.readline
#
# N=int(input())
# s=list(map(int,input().split()))
# t=int(input())
# print(s.count(t))
# import sys
#
# input=sys.stdin.readline
#
# N=[0]*31
# N[0]=1
# for i in range(28):
#     N[int(input())]=1
# c=0
# for j in range(1,31):
#     if N[j]==0:
#         c+=1
#         print(j)
#     if c==2:
#         break
# import sys
#
# input=sys.stdin.readline

# N,M=map(int,input().split())
# A=[]
# for i in range(N):
#     A.append(list(map(int,input().split())))
# B=[]
# for j in range(N):
#     b=list(map(int,input().split()))
#     A[j]=[A[j][k]+b[k]for k in range(M)]
# for a in A:
#     aa=" ".join(str(s) for s in a)
#     print(aa)
# import sys
#
# input=sys.stdin.readline
#
# print(ord(input().strip()))
# import sys
#
# input = sys.stdin.readline
# print(len(input().strip()))
# import sys
#
# input = sys.stdin.readline
# s=input().strip()
# w=[-1]*26
# for i in range(len(s)):
#     q=ord(s[i])-97
#     if w[q]==-1:
#         w[q]=i
# for i in w:
#     print(i,end=' ')
# import sys
#
# input = sys.stdin.readline
# s=input().strip()
# e=''
# for i in s:
#     if ord(i)>=97:
#         e+=chr(ord(i)-32)
#     else:
#         e+=chr(ord(i)+32)
# print(e)
# import sys

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
# import sys
#
# input=sys.stdin.readline
#
# for i in range(int(input())):
#     a=input().strip()
#     print(a[0]+a[-1])
# import sys
#
# input=sys.stdin.readline
# a,b=map(int,input().split())
# print((a+b)*(a-b))
import sys

input=sys.stdin.readline
nums=list(map(int,input().split()))
print(sum(s**2 for s in nums)%10)