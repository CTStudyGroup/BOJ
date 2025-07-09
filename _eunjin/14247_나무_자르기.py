import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))
arr = []
for i in range(N):
    arr.append((A[i], H[i]))

# 많이 자라는 애들은 최대한 뒤에 잘라서 최대한 많이 자란 상태에서 자르기
# 조금 자라는 애를 먼저 자르기
arr.sort(key=lambda x: x[0])

answer = 0
for i in range(N):
    a, h = arr[i]
    answer += h + a * i

print(answer)
