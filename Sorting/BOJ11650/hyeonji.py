import sys
input=sys.stdin.readline

n=int(input())

info=[]
for i in range(n):
    info.append(list(map(int,input().split())))

info.sort(key=lambda x:(x[0],x[1]))

for i in info:
    print(*i)
    
    
# import sys
# input=sys.stdin.readline

# n=int(input())
# arr=[]

# for i in range(n):
# 	x,y=map(int,input().split())
# 	arr.append((x,y))

# arr.sort()

# for i in arr:
# 	print(i[0],i[1])