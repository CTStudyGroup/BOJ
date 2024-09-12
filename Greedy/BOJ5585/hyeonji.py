import sys
input=sys.stdin.readline

money=int(input())       # 지불할 돈
change=1000-money        # 거스름 돈
arr=[500,100,50,10,5,1]

cnt=0                    # 잔돈의 개수
for i in arr:
    if change==0:
        break
    cnt+=change//i
    change=change%i

print(cnt)