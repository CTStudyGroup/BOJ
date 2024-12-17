n,m=map(int,input().split())
info=[]

for i in range(n):
    info.append(input())

dna=''
answer=0
for i in range(m):
    cnt={}
    for j in range(n):
        if info[j][i] not in cnt:
            cnt[info[j][i]]=1
        else:
            cnt[info[j][i]]+=1
    sorted_cnt=dict(sorted(cnt.items(), key=lambda item:(-item[1],item[0])))
    dna+=list(sorted_cnt.keys())[0]
    for j in range(1,len(sorted_cnt)):
        answer+=list(sorted_cnt.values())[j]

print(dna)
print(answer)