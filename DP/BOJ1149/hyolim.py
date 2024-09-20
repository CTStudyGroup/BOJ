'''
DP[i]=DP[i-1]+min(arr[i])
초기값 설정을 잘해야함
초기값 : 모든 비용 중에 가장 작은 값
2차원 배열에서 최솟값을 중심으로 각 집의 비용을 정렬함
최솟값을 시작으로 DP 관계식 수행
'''

# 막혔다..................................
# 정렬하고 이웃이고 같은 색인지 확인한 후에 진행해야하는데 ... 정렬을 안하면 가장 최솟값을 못구한다.
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]

''' input print
print(N)
for i in arr:
	for j in i:
		print(j,end=" ")
	print()
'''

# 정렬하면 안됨... i 순서가 뒤바뀜..
print(min(arr),arr.index(min(arr)))

print(arr)
# min(arr)할 때 arr이 2차원일 경우 0으로만 비교해서 확인한다... 이런 개씝썅
# 내장함수 사용하면 안되고 직접 만들어서 사용해야함
def find_min(_arr):
	min_val=9999;
	idx1=-1;
	idx2=-1;

	for i in range(0,len(_arr)):
		for j in range(0,len(_arr[i])):
			if(min_val>_arr[i][j]):
				min_val=arr[i][j]
				idx1=i
				idx2=j
	return min_val, idx1, idx2

DP,idx,rgbIdx=find_min(arr)
rem_rgbIdx=rgbIdx; # 나중에 기억하기 위함
# DP 초기값이 있는 집 번호 = idx
# 무슨 색으로 했는지 알려주는 인덱스 = rgbIdx

# 초기값이 있는 DP 보다 큰 쪽 계산
for i in range(idx+1,N):
	# DP에 들어갔던 이전 인덱스와 겹치면 안됨
	arr[i][rgbIdx]=9999; # 초기값을 아예 설정하지 못하도록 막아놓기

	DP+=min(arr[i])
	rgbIdx=arr[i].index(min(arr[i]))
	print(DP, end=" ")
	print(rgbIdx)
print("=================")

# 중간에 초기화해줘야함
rgbIdx=rem_rgbIdx # 무슨 색으로 했는지 알려주는 인덱스

# 초기값이 있는 DP 보다 작은 쪽 계산
for i in range(idx-1,-1,-1):
	# DP에 들어갔던 이전 인덱스와 겹치면 안됨
	arr[i][rgbIdx]=9999; # 초기값을 아예 설정하지 못하도록 막아놓기

	DP+=min(arr[i])
	rgbIdx=arr[i].index(min(arr[i]))
	print(DP, end=" ")
	print(rgbIdx)


	