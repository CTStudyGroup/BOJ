from collections import deque
import sys
input=sys.stdin.readline

N,M=map(int,input().split())

arr=[[0 for _ in range(N+1)]]+[[0]+list(map(int,input().split())) for _ in range(N)]

blizard=[map(int,input().split()) for _ in range(M)]

dx=[0,-1,1,0,0]
dy=[0,0,0,-1,1]
# 1 2 3 4

m_set=[0,0,0,0]
biz_list=deque()
def cal_biz_list(type):
    global biz_list

    s_x=1
    s_y=0
    tmp=N
    # 오른쪽 아래쪽 왼쪽 오른쪽
    # 7 6 6 5 가고
    # 5 4 4 3 가고
    # 3 2 2 1 가고
    cnt_lst=[N,N-1,N-1,N-2]
    cnt_start=0
    di_x=[0,1,0,-1]
    di_y=[1,0,-1,0]
    if type==0:
        # 갖고와서 처리하는 용
        biz_list = deque()
        while 1:
            if s_x==(N+1)//2 and s_y==(N+1)//2 -1 :
                break
            for i in range(4):
                cnt_start+=2
                for k in range(cnt_lst[i]):
                    s_x+=di_x[i]
                    s_y+=di_y[i]

                    biz_list.append(arr[s_x][s_y])
            cnt_lst=[i-2 for i in cnt_lst]
    else:
        # 처리 후 다시 저장하는용
        cnt=0
        while 1:
            if s_x == (N + 1) // 2 and s_y == (N + 1) // 2 - 1:
                break
            for i in range(4):
                cnt_start += 2
                for k in range(cnt_lst[i]):
                    s_x += di_x[i]
                    s_y += di_y[i]

                    arr[s_x][s_y]=biz_list[cnt]
                    cnt+=1
            cnt_lst = [i - 2 for i in cnt_lst]
def break_number(d,s):
    c=[(N+1)//2 , (N+1)//2]
    for i in range(1,s+1):
        c[0]+=dx[d]
        c[1]+=dy[d]
        arr[c[0]][c[1]]=0

def biz_fill():
    global biz_list
    biz_list_tmp=deque()
    cnt=0
    for i in range(N*N-1):
        if biz_list[i]!=0:
            biz_list_tmp.append(biz_list[i])
        else:
            cnt+=1
    for _ in range(cnt):
        biz_list_tmp.append(0)

    biz_list=biz_list_tmp

def destroy_biz():
    global biz_list,m_set
    while_check=1

    while while_check==1:
        # 폭발시키기 위해 arr에서 가져오기
        cal_biz_list(0)
        # 같은 숫자 지우기 위해 역순
        biz_list.reverse()
        while_check=0
        cnt=1
        tmp=biz_list[0]
        start=0
        for i in range(1,len(biz_list)):
            if biz_list[i]==tmp:
                cnt+=1
            else:
                if cnt>=4:
                    while_check=1

                    m_set[biz_list[start]]+=cnt
                    for k in range(start,i):
                        biz_list[k]=0

                cnt=1
                start=i
                tmp=biz_list[i]
        # 이 시점에서 biz fill 8개 삭제되어야함

        # 0 지우고 뒤에 채워넣기
        biz_fill()
        # 채워넣기전 돌리기
        biz_list.reverse()
        # 다시 넣기
        cal_biz_list(1)


def grouping():
    global biz_list
    biz_list_tmp=deque()
    # arr -> biz_list 로 갖고와서  00 이 먼저
    cal_biz_list(0)
    # biz list 역순으로 돌리고 (돌리는 이유는 채우기 용)
    biz_list.reverse()

    cnt=1
    tmp=biz_list[0]
    for i in range(1,len(biz_list)):
        # 연속그룹일때
        if tmp==biz_list[i]:
            cnt+=1
        else:
            # 다른게 나왔을 때 현재까지 기준으로 append
            biz_list_tmp.append(cnt)
            biz_list_tmp.append(tmp)

            tmp=biz_list[i]
            cnt=1
        if len(biz_list_tmp) > N*N:
            break
    while 1:
        if len(biz_list_tmp)>N*N-1:
            break
        biz_list_tmp.append(0)

    biz_list=deque(biz_list_tmp[i] for i in range(N*N-1))

## 블리자드 처리
for d,s in blizard:

    # arr에서 삭제하고
    break_number(d,s)

    # arr -> biz_list 로 갖고와서  00 이 먼저
    cal_biz_list(0)
    # biz list 역순으로 돌리고 (돌리는 이유는 채우기 용)
    biz_list.reverse()
    # 0 지우기
    biz_fill()
    # 채워넣기 전 돌리기
    biz_list.reverse()
    # 다시 채워넣기
    cal_biz_list(1)


    # 연속폭발

    destroy_biz()

    # 그룹 지어서 append 하기
    grouping()
    # 다시 arr 에 넣어야한다. 앞자리 부 터 시작하는중
    biz_fill()
    biz_list.reverse()
    # 다시 채워넣기
    cal_biz_list(1)

print(m_set[1]+m_set[2]*2+m_set[3]*3)
