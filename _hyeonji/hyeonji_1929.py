import sys
import math
input=sys.stdin.readline

m,n=map(int,input().split())
arr=[0]*(n+1)

for i in range(2,n+1):
	arr[i]=i

for i in range(2,int(math.sqrt(n))+1):
	if(arr[i]==0):
		continue
	for j in range(2*i,n+1,i):
		arr[j]=0

for i in range(m,n+1):
	if(arr[i]!=0):
		print(arr[i])