#input
n=int(input())
A=map(int,input().split())
B=map(int,input().split())

A=sorted(A)
B=sorted(B,key=lambda x : -x)
ans=0
for i in range(n):
	ans+=A[i]*B[i]

print(ans)