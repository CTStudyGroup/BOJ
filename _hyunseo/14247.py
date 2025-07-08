# 250709 : [BOJ 14247] 나무 자르기 #1392

# 나무의 개수
n = int(input())

# 첫날 나무의 길이
H = list(map(int, input().split()))

# 나무들이 자라는 길이
A = list(map(int, input().split()))

# n = 5
# H = [1,3,2,4,6]
# A= [2,7,3,4,1]
answer = sum(H)
for idx, val in enumerate(sorted(A)) :
    answer += (idx)*val
print(answer)
