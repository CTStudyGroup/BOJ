# 입력 받기
N, H = map(int, input().split())

odd = [0]*(H+1)  # 길이가 x 인 석순의 개수
even = [0]*(H+1)  # 길이가 x인 종유석의 개수

for i in range(1, N+1):
    x = int(input())
    if(i % 2 == 0):
        even[x] += 1
    else:
        odd[x] += 1
# print("odd:", odd)
# print("even:", even)

dp = [0]*(N+1)  # 높이가 x일 때 장애물의 개수

min_value = int(1e12)
min_cnt = 0

value = N//2  # 높이가 1일 때의 기본 장애물 개수
for x in range(1, H+1):
    value -= odd[x-1]
    value += even[H-x+1]
    if min_value == value:  # 얘가 최소 구간인 경우 개수 카운트
        min_cnt += 1
    elif min_value > value:
        min_value = value
        min_cnt = 1


print(min_value, min_cnt)
