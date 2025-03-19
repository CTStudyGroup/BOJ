from sys import stdin as s
s = open("txt/1027.txt", 'r')

N = int(s.readline())

b = list(map(int, s.readline().split()))

see = [0] * N

trans_flag = 0

for i in range(N):
    #왼쪽 탐색
    start = b[i]
    cnt = 0
    trans_flag = 0
    for l in range(i,0):
        pass

    #오른쪽 탐색
    for r in range(i+1,N):
        if trans_flag == 0: #작은 거 수행 if start > b[i]:
            if start < b[r]:
                trans_flag = 1
                sub = start - b[r] # sub 갱신
                last = b[i]

            else:
                sub = start - b[r] # 현재 차이
                pass

        if trans_flag == 1:
            #print("hi")
            c_sub = b[r] - last #처음에는 0
            if sub < c_sub:
                #만약 기존 차이보다, 현재의 차이가 더 크면 ++ 기존 차이 갱신
                cnt += 1
                last = b[r]
                sub = c_sub
    print(cnt)
    break

# 완전탐색

# 1 5 3 2 6 7 8 9 10