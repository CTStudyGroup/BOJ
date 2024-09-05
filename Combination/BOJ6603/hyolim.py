
from itertools import combinations

while True:
	L = list(map(int,input().split()))
	N = L[0]
	if(N == 0):
		break;
	arr = L[1:]

	ans = list(combinations(arr,6))

	for i in ans:
		for j in i:
			print(j,end=' ')
		print()
	print()