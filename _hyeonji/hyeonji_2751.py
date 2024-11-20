import sys
input=sys.stdin.readline

n=int(input())
nums=[]

for i in range(n):
	num=int(input())
	nums.append(num)

nums.sort()

for i in nums:
        print(i)