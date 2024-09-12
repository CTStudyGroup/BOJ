import sys
input=sys.stdin.readline

def dfs(n,idx):
    global cnt
    if n==0:
        cnt+=1
        return
    for i in range(26):
        if alpha[i]>0 and i!=idx:
            alpha[i]-=1
            dfs(n-1,i)
            alpha[i]+=1

s=list(input().rstrip())

alpha=[0]*26
cnt=0

for i in range(len(s)):
    alpha[ord(s[i])-97]+=1

dfs(len(s),-1)

print(cnt)