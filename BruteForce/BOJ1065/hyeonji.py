import sys
input=sys.stdin.readline

def check(num):
    if 1<=num<100:
        return 1
    else:
        arr=list(map(int,str(num)))
        d=arr[1]-arr[0]
        ccnt=0
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i]!=d:
                continue
            else:
                ccnt+=1
        if ccnt==int(len(str(num)))-2:
            return 1
        else:
            return 0

n=int(input())

cnt=0
for i in range(1,n+1):
    cnt+=check(i)

print(cnt)