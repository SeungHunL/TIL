T = int(input())
for test_case in range(1, T + 1):
    X, Y = map(float, input().split()) 
    h1 = ((X + Y) + (X ** 2 - X * Y + Y ** 2) ** 0.5) / 6
    h2 = ((X + Y) - (X ** 2 - X * Y + Y ** 2) ** 0.5) / 6
    V1 = h1*(X-2*h1)*(Y-2*h1)
    V2 = h2*(X-2*h2)*(Y-2*h2)
    print(h1,X-2*h1,Y-2*h1)
    print(h2,X-2*h2,Y-2*h2)
    ans = V1 if V1 >= V2 else V2
    print(f'#{test_case} {ans:.6f}')