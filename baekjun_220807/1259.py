import sys

input = sys.stdin.readline

while 1:
    nums = input().strip()
    if nums == "0":
        break
    for i in range(len(nums)):
        if nums[i]!=nums[-(i+1)]:
            print("no")
            break
    else:
        print("yes")