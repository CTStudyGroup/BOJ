N = int(input())
arr = list(map(int, input().split()))
X = int(input())

# 딕셔너리로 각 숫자의 개수 세기
_dict = {}

for elem in arr:
    if elem in _dict:
        _dict[elem] += 1
    else:
        _dict[elem] = 1

answer = 0
for key in _dict.keys():
    if X - key in _dict:
        if 2 * key == X:
            if _dict[X - key] > 1:
                answer += 1
        else:
            answer += 1

print(answer // 2)
