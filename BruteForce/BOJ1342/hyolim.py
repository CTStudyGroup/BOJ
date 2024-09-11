# 1. 메모리초과
# 입력 받은 문자열을 하나씩 다 뗀 후에 
# 순열로 엮어서
# 조건에 맞는지 확인하기
from itertools import permutations

str=input()

answer=set();
for i in permutations(str):
	isOk=True;
	for j in range(len(i)-1):
		# 만약 같은게 하나라도 있을 경우 패스..
		if(i[j]==i[j+1]):
			isOk=False;
		
		# print(j,end='')

	if(isOk):
		answer.add(i)
	# print()

# for i in answer:
# 	print(i)
	
print(len(answer))