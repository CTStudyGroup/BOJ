import sys
input=sys.stdin.readline

def fac(num):
    if num==0:
        return 1
    else:
        for i in range(num-1,0,-1):
            num*=i
        return num

n= int(input())
value=fac(n)
arr=list(str(value))

count=0
for i in range(len(arr)-1,-1,-1):
    count+=1
    if arr[i]!="0":
        break

print(count-1)