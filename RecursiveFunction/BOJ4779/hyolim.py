# function
def func(depth,isPrint):
	if(depth==0):
		if(isPrint):
			print("-",end="");
		else:
			print(" ",end="");
		return;
	if(isPrint):
		func(depth-1,True)
		func(depth-1,False)
		func(depth-1,True)
	else:
		func(depth-1,False)
		func(depth-1,False)
		func(depth-1,False)

# input 
while True:
	try:
		N = int(input())
		func(N,True)
		print("");
	except:
		break;




