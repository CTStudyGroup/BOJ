'''
1. 정렬 후, 양수랑 음수를 나눈다.
2. 각 리스트에서 최댓값이 어떤게 더 큰지 확인한다. 
가장 큰 수를 마지막에 빼야한다. 왜냐하면 문제에서 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요가 없다고 했기 때문이다.
3. 그리고 최댓값으로부터 M만큼 인덱스를 돌아서 걸음수를 2 곱해서 저장한다.
4. 마지막에 M보다 작을 경우 남은 애들 중에서 가장 큰 수를 2 곱해서 더한다.
'''

# input
N,M=map(int,input().split())
arr=list(map(int,input().split()))

# 1. 정렬
arr = sorted(arr)

# 2. 절댓값의 최댓값 찾기
if(abs(arr[0])>abs(arr[-1])):
	maxN=abs(arr[0])
else:
	maxN=abs(arr[-1])

# 3. 배열을 양수, 음수 나누기
plus=[]
minus=[]
for i in arr:
	if(i>0):
		plus.append(i)
	else:
		minus.append(abs(i))

minus=sorted(minus)

# for i in minus:
# 	print(i,end=" ")
# print()

# 4. 최댓값으로부터 M만큼 인덱스 돌기
answer=0
# (1) plus
pidx=len(plus)-1

while(pidx>=M):
	answer+=2*plus[pidx]
	pidx=pidx-M;
	# print(answer, pidx)
if(pidx>=0):
	answer+=2*plus[pidx]
# print(answer, pidx)

# minus일 때도 plus와 마찬가지로 가장 많이 움직일 때 최대한 많은 책을 가져가야하므로 
# minus를 단순히 abs해서 더하는게 아니라 아예 처음부터 양수인 배열로 만들어야함
midx=len(minus)-1

while(midx>=M):
	answer+=2*minus[midx]
	midx=midx-M;
	# print(answer, midx)
if(midx>=0):
	answer+=2*minus[midx]
# print(answer, midx)

# 5. 가장 큰 최댓값 없애기
answer-=maxN
print(answer)
