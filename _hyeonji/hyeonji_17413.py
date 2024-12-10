s=input()

stack=[]
answer=[]

for i in s:
    if i=='<' and len(stack)!=0:
        stack.reverse()
        answer.append(''.join(stack))
        stack=[]
        stack.append(i)
    elif i=='>':
        stack.append(i)
        answer.append(''.join(stack))
        stack=[]
    elif i==' ' and '<' not in stack:
        stack.reverse()
        stack.append(' ')
        answer.append(''.join(stack))
        stack=[]
    else:
        stack.append(i)

if len(stack)==0:
    for i in answer:
        print(i,end='')
else:
    stack.reverse()
    answer.append(''.join(stack))
    for i in answer:
        print(i,end='')