from itertools import combinations

n,s=map(int,input().split())

arr=list(map(int,input().split())) 
cnt=0;

for i in range(1,n+1):
	comb=combinations(arr,i)
	for j in comb:
		# print(j)
		summ=0;
		for m in j:
			summ+=m;
		# print(summ)
		if(summ==s):
			cnt+=1;

print(cnt);

		