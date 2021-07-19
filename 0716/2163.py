Q, W =input().split()
Q = int(Q)
W = int(W)
if Q>=W:
    R=(Q-1)+(W-1)*Q
else:
    R=(W-1)+(Q-1)*W
print(R)