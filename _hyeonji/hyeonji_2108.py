import sys
input=sys.stdin.readline

n=int(input())

nums=[]
set_nums=set()
dic_nums=dict()
for i in range(n):
    num=int(input())
    nums.append(num)
    if num in set_nums:
        dic_nums[num]+=1
    else:
        dic_nums[num]=1
    set_nums.add(num)

# 산술평균
avg=sum(nums)/len(nums)
print(round(avg))

# 중앙값
nums.sort()
mid=(len(nums)//2)+1
print(nums[mid-1])

# 최빈값
result=sorted(dic_nums.items(),key=lambda x:(-x[1],x[0]))
if len(result)==1:
    print(result[0][0])
else:
    if result[0][1]==result[1][1]:
        print(result[1][0])
    else:
        print(result[0][0])
# 범위
print(max(nums)-min(nums))