import sys
input=sys.stdin.readline

k=int(input())

result=[]
for i in range(k):
    num=int(input())
    if num==0:
        result.pop()
    else:
        result.append(num)
print(sum(result))