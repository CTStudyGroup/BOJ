N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]

arr=sorted(arr);

for i,j in arr:
	print(i,j)