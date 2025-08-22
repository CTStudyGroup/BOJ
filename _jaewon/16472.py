# 투 포인터 사용
# 인식할 수 있는 문자열의 최대 길이 출력
# 문자열의 최대 길이는 100,000
from collections import defaultdict
import sys
N = int(input())
string = sys.stdin.readline().rstrip()

# maximum = 0

# length = len(string)
# start = 0
# end = 1

# maximum = 1
# while start < length and end <= length:
#     tmp = string[start:end]
#     if(len(set(tmp)) > N):
#         start += 1
#     else:
#         maximum = max(maximum, end - start)
#         end += 1
        
# print(maximum)

# 문자열의 slicing은 O(N)
# set도 O(N)




length = len(string)
start = 0
end = 0

maximum = 1
window = defaultdict(int)  # 윈도우 안 문자 -> 빈도수
window[string[start]] += 1

while start < length and end < length:
    end += 1
    if end == length:
        break

    # 새로운 문자 추가
    window[string[end]] += 1

    # 알파벳 종류가 N을 넘으면 왼쪽을 줄이기
    while len(window) > N:
        window[string[start]] -= 1
        if window[string[start]] == 0:
            del window[string[start]]
        start += 1

    maximum = max(maximum, end - start + 1)

print(maximum)
