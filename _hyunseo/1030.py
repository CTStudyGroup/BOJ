'''
time 0 : 흰색 정사각형 하나
time 1 : 흰색 정사각형 하나가 3*3으로 나뉨. 
         근데 나누어진 정사각형이 흰색이라 가운데 1*1이 정사각형
         w w w 
         w b w 
         w w w 
time 2 : 정사각형 하나씩 3*3으로 또 나뉨.
         w -> www
              wbw
              www으로
         b -> bbb
              bbb
              bbb
으로 나뉨. 

'''
# w = 0 b = 1
# 시간 s일 때, R1C1부터 R2C2까지 출력
s, N, K, R1, R2, C1, C2 = map(int, input().split())

def something(i, j, t) :
    unit = N**(t-1)
    start = (N - K) // 2
    # 수식
    if (start * unit) <= i < ((start + K) * unit) and (start * unit) <= j < ((start + K) * unit):
        return 1
    if t == 0 : return 0
    return something(i % unit, j % unit, t - 1)
for i in range(R1, R2 + 1) :
    for j in range(C1, C2 + 1) :
        print(something(i, j, s), end='')
    print()
        
