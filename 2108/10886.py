T = int(input())
no = cute = 0
for num in range(T):
    if input() == '1':
        cute += 1
    else:
        no += 1
if cute < no:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
