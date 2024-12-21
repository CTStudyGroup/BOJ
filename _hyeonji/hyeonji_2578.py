def check(val):
    # 가로
    for i in range(5):
        if bingo[i]==[0,0,0,0,0]:
            val+=1
    # 세로
    for i in range(5):
        cnt=0
        for j in range(5):
            if bingo[j][i]==0:
                cnt+=1
        if cnt==5:
            val+=1
    # 대각선
    cnt1=0
    for i in range(5):
        if bingo[i][i]==0:
            cnt1+=1
    if cnt1==5:
        val+=1


    cnt2=0
    for i in range(5):
        if bingo[i][4-i]==0:
            cnt2+=1
    if cnt2==5:
        val+=1

    return val

bingo=[list(map(int,input().split())) for i in range(5)]

answer=[]
for i in range(5):
    answer+=list(map(int,input().split()))

val=0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if bingo[x][y]==answer[i]:
                bingo[x][y]=0
    if check(val)>=3:
        print(i+1)
        break