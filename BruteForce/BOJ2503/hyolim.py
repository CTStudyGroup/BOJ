'''
스트라이크 볼 게임 생각하듯이 개발하면 머리 터진다.
111부터 999까지 다 돌려보면 9*9*9 시간 복잡도 가능
a 스트라이크 b 볼 계산해서 맞는거 나오면 cnt++

'''
n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
answer=0

def isCheck(n1,n2,n3,m,strike,ball):
	temp_strike=0;
	temp_ball=0;

	m1=m//100
	m2=((m%100)-(m%10))//10
	m3=m%10;

	# strike
	if(n1==m1):
		temp_strike+=1;
	if(n2==m2):
		temp_strike+=1;
	if(n3==m3):
		temp_strike+=1;

	# print(temp_strike);

	# ball
	if(n1==m2 or n1==m3):
		temp_ball+=1;
	if(n2==m1 or n2==m3):
		temp_ball+=1;
	if(n3==m1 or n3==m2):
		temp_ball+=1;

	# print(temp_ball);

	if(strike==temp_strike and temp_ball==ball):
		return True;
	else:
		return False


for a in range(1,10):
	for b in range(1,10):
		for c in range(1,10):
			if(a==b or a==c or b==c):
				continue;
			isTrue=True;
			for i in arr:
				if not isCheck(a,b,c,i[0],i[1],i[2]):
					isTrue=False;
			if(isTrue):
				answer+=1


print(answer)
