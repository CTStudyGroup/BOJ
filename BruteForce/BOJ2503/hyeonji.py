import sys
input=sys.stdin.readline

def func(k,num,s,b):
    strike=0
    ball=0

    k_=list(map(int,str(k)))
    num_=list(map(int,str(num)))

    for i in range(3):
        if k_[i]==num_[i]:
            strike+=1
        else:
            if k_[i] in num_:
                ball+=1

    if strike==s and ball==b:
        return 1
    else:
        return 0

n=int(input())
nums=[1]*1000

for i in range(n):
    num,s,b=map(int,input().split())
    for j in range(1000):
        # 세 자리수
        if j<100:
            nums[j]=0
        # 1에서 9까지의 수
        elif 0 in list(map(int,str(j))):
            nums[j]=0
        # 서로 다른 수
        elif len(set(list(map(int,str(j))))) != len(list(map(int,str(j)))):
            nums[j]=0
        elif nums[j]==1:
            nums[j]=func(j,num,s,b)

print(sum(nums))