from itertools import combinations

#input
I = list(map(int,input().split()))
arr = list(map(str,input().split()))
arr = sorted(arr)
L = I[0]
C = I[1]

# 조건에 맞는지 확인하는 함수
def isTrue(ar):
	acnt=0 # 모음 카운트
	bcnt=0 # 자음 카운트
	for i in ar:
		if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u'):
			bcnt+=1
		else:
			acnt+=1
	# print(acnt, bcnt)
	if(acnt>=1 and bcnt>=2):
		return True;
	else:
		return False;

# 조합 생성
CList=combinations(arr,L);

# 조건에 맞는 애들만 출력
for i in CList:
	if(isTrue(i)):
		for j in i:
			print(j,end='')
		print()
	


