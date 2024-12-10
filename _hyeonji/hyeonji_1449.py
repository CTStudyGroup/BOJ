n,l=map(int,input().split())
info=list(map(int,input().split()))

info.sort()

start=info[0]
cnt=1
for i in range(1,len(info)):
    if (info[i]+0.5)-(start-0.5)<=l:
        continue
    else:
        start=info[i]
        cnt+=1

print(cnt)