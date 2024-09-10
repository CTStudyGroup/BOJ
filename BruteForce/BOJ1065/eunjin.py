# 입력 받기
N = int(input())

if(N < 100):
    print(N)
else:
    cnt = 0
    arr = [i for i in range(100, N+1)]
    for elem in arr:
        elem = str(elem)
        ok = True
        diff = int(elem[0])-int(elem[1])
        for i in range(len(elem)-1):
            if(int(elem[i])-int(elem[i+1]) != diff):
                ok = False
                break
        cnt += ok
    print(99+cnt)
