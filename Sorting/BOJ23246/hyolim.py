
n=int(input())

info=[list(map(int,input().split())) for _ in range(n)]

info = sorted(info,key=lambda x:(x[1]*x[2]*x[3],x[1]+x[2]+x[3],x[0]))

for i,j,k,m in info[:3]:
	print(i,end=' ')