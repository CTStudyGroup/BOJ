import sys
input=sys.stdin.readline

test=list(map(str,input().split("-")))
result=0

def Sum(a):
	sum=0
	seg=str(a).split("+")

	for i in seg:
		sum+=int(i)

	return sum

for i in range(len(test)):
	seg2=Sum(test[i])
	if i==0:  
		result+=seg2
	else:
		result-=seg2

print(result)