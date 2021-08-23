equation=input()
stack1=[]
stack2=[]
for i in range(len(equation)):
    if equation[i] in ('(','+','-','*'):
        stack1.append(equation[i])
    elif equation[i]==')':
        while 1:
            if stack1[-1]!='(':
                stack2.append(stack1.pop())
            else:
                stack1.pop()
                break
    elif equation[i]=='/':
        while 1:
            print(stack1)
            if stack1[-1]=='+'or stack1[-1]== '-':
                stack2.append(stack1.pop())
                break
            else:
                stack2.append(stack1.pop())
    else:
        stack2.append(equation[i])
print(stack1)
print(stack2)