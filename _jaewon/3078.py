# 등수의 차이가 K보다 작거나 같음.
# 이름의 길이가 같음.
# N은 300,000까지
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
name_length = []

for _ in range(N):
    name_length.append(len(input().strip()))  # 개행 제거 주의

dic = {}
for index, length in enumerate(name_length):
    if length not in dic:
        dic[length] = []
    dic[length].append(index)

total = 0
for length in dic:
    arr = dic[length]  # 같은 이름 길이의 인덱스 배열 (이미 정렬됨)
    j = 0
    for i in range(len(arr)):
        while j < len(arr) and arr[j] - arr[i] <= K:
            j += 1
        total += (j - i - 1)  # i와 j 사이에 있는 원소들이 모두 조건 만족

print(total)
