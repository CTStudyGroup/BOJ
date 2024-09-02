# 나의 풀이
def recursive(n):
	if(n==0):
		return 0;
	elif(n==1):
		return 1;
	return recursive(n-1)+recursive(n-2);

n = int(input());
print(recursive(n));


# 다른 풀이
# def fibo(x):
# 	global arr;

# 	if(arr[x]!=-1):
# 		return arr[x];

# 	arr[x] = fibo(x-1) + fibo(x-2);
# 	return arr[x]

# x = int(input())

# arr = [-1]*(x+2)
# arr[0] = 0
# arr[1] =1

# print(fibo(x))
