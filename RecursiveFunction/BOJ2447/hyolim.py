n=int(input())

answer=[[' ' for _ in range(n)] for _ in range(n)]

def star(depth,row,col,isStar):
	global answer
	if(depth==1):
		if(isStar):
			answer[row][col]='*'
		else:
			answer[row][col]=' '
		return

	if(isStar):
		star(depth//3,row+0,col+0,True)
		star(depth//3,row+0,col+depth//3,True)
		star(depth//3,row+0,col+depth//3*2,True)

		star(depth//3,row+depth//3,col+0,True)
		star(depth//3,row+depth//3,col+depth//3,False)
		star(depth//3,row+depth//3,col+depth//3*2,True)

		star(depth//3,row+depth//3*2,col+0,True)
		star(depth//3,row+depth//3*2,col+depth//3,True)
		star(depth//3,row+depth//3*2,col+depth//3*2,True)



star(n,0,0,True)

for i in range(n):
	for j in range(n):	
		print(answer[i][j],end='')
	print()
