import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())
arr = []
_dict = {}

for _ in range(N):
    n = int(input())
    arr.append(n)

    if n in _dict:
        _dict[n] += 1
    else:
        _dict[n] = 1

# 1. 산술평균 출력
print(int(round(sum(arr)/len(arr), 0)))

# 2. 중앙값 출력
arr.sort()
print(arr[int(len(arr)/2)])

# 3. 최빈값 출력
max_freq = max(_dict.values())
temp_arr = []

for key, value in _dict.items():
    if value == max_freq:
        temp_arr.append(key)

if len(temp_arr) == 1:
    print(temp_arr[0])
else:
    print(sorted(temp_arr)[1])

# 4. 범위 출력
print(arr[-1]-arr[0])
