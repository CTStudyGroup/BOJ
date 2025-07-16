import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
T = [input().strip() for _ in range(N)]

# 각 단어마다 각 문자열을 key로 하는 해시맵에 본인 인덱스 저장
_dict = defaultdict(list)

for n in range(N):
    word = T[n]
    for i in range(1, len(word) + 1):
        curr = word[:i]
        _dict[curr].append(n)

# dict를 1.key 문자열 길이 내림차순, 2.key가 저장된 순서 오름차순으로 정렬 (S 조건)
for i, key in sorted(enumerate(_dict.keys()), key=lambda x: [-len(x[1]), x[0]]):
    if len(_dict[key]) >= 2:
        print(T[_dict[key][0]])
        print(T[_dict[key][1]])  # T 조건
        exit()
