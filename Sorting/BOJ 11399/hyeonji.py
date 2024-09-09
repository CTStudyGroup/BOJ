import sys
input=sys.stdin.readline

n=int(input())
time=list(map(int,input().split()))

time.sort()

total_time=0
total_arr=[]
for i in time:
    total_time+=i
    total_arr.append(total_time)

answer = sum(total_arr)  # 각 사람이 돈을 인출하는데 필요한 시간의 합
print(answer)