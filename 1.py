result=str(input())
back=""
i=len(result)
for i in range(0,len(result)):
    back+=result[len(result)-i-1]
print(back)
if(result==back):  
    print("입력하신 단어는 회문(Palindrome)입니다.")
    print("하.")
    print("하.")