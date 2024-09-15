#input
n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]

blue=0
white=0

#solve
#모든 칸이 같은 색인지 판별하는 함수
def isColor(y,x,num):
	for i in range(num):
		for j in range(num):
			if(arr[y][x] != arr[y+i][x+j]):
				return False

	return True

# 재귀함수
def func(y,x,num):
	global blue,white
	if(isColor(y,x,num)):
		if(arr[y][x]==1):
			blue+=1
		else:
			white+=1
		return
	func(y,x,num//2)
	func(y,x+num//2,num//2)
	func(y+num//2,x,num//2)
	func(y+num//2,x+num//2,num//2)

func(0,0,n)
print(white)
print(blue)
