"""
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
"""
import sys

input1 = int(input())

# 10이 됐을 때 return
# 1부터 시작 전이랑 전전을 알아야하는데 귀찮 굳이 알아야하나 final에서 n을 빼면 될 것 같은데 

 
def func(prev,cur,n,final_n):
	# print(prev,cur,n,final_n)
	sum=prev+cur;

	if(n==final_n):
		print(sum);
		return;

	func(cur,sum,n+1,final_n);

if(input1 == 0):
	print(0);
elif(input1 == 1 or input1 == 2):
	print(1);
else:
	func(1,1,3,input1)
