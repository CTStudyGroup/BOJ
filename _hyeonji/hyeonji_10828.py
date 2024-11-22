import sys
input=sys.stdin.readline

n=int(input())
stack=[]

for i in range(n):
    test=input().split()
    order=test[0]
    if order=="push":
        value=test[1]
        stack.append(value)
    elif order=="pop":
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif order=="size":
        print(len(stack))
    elif order=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif order=="top":
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)