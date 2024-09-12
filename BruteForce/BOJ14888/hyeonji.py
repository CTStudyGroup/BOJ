import sys
input=sys.stdin.readline

def dfs(now,val):
    global minimum,maximum,add,sub,mul,div

    if val==n:
        minimum=min(minimum,now)
        maximum=max(maximum,now)
    else:
        if add>0:
            add-=1
            dfs(now+num[val],val+1)
            add+=1
        if sub>0:
            sub-=1
            dfs(now-num[val],val+1)
            sub+=1
        if mul>0:
            mul-=1
            dfs(now*num[val],val+1)
            mul+=1
        if div>0:
            div-=1
            dfs(int(now/num[val]),val+1)
            div+=1

n=int(input())
num=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

minimum=1e9   # 최소
maximum=-1e9  # 최대

dfs(num[0],1)

print(int(maximum))
print(int(minimum))