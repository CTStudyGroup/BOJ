# 1. 메모리초과
# 입력 받은 문자열을 하나씩 다 뗀 후에 
# 순열로 엮어서
# 조건에 맞는지 확인하기

# 2. 재귀 구현해서 같은 문자가 발생할 경우 중간에 가지치기

str=input();
ans=set();
visited=[False for _ in range(len(str))]

def permutation(depth,curStr):

	# 가지치기
	if(len(curStr)>1):
		if(curStr[-1]==curStr[-2]):
			return;

	if(depth==len(str)):
		# print(curStr)
		ans.add(curStr);
		return;


	for i in range(0,len(str)):
		if not visited[i]:
			visited[i]=True
			permutation(depth+1,curStr+str[i])
			visited[i]=False

permutation(0,'')

# print()
# for i in ans:
# 	print(i)

print(len(ans))



