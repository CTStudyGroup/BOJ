from string import ascii_lowercase
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
words = [input().strip() for _ in range(N)]

# 예외 처리
if K < 5:
    print(0)
    exit()
if K == 26:
    print(N)
    exit()

# 배운 필수 알파벳
essential = {'a', 'n', 't', 'i', 'c'}

# 단어에서 필수 알파벳 제거한 나머지를 저장
processed = [set(word) - essential for word in words]

# 배울 수 있는 후보 알파벳
candidates = sorted(set(ascii_lowercase) - essential)  # ['b', 'd', 'e', ..., 'z'] 중 21개

answer = 0

def dfs(index, arr):
    global answer
    if len(arr) == K:
        learned = set(arr)
        cnt = 0
        for word in processed:
            if word <= learned:  # word의 알파벳들이 전부 learned에 포함될 때
                cnt += 1
        answer = max(answer, cnt)
        return

    for i in range(index, len(candidates)):
        arr.append(candidates[i])
        dfs(i + 1, arr)
        arr.pop()

# 필수 알파벳 5개부터 시작
dfs(0, ['a', 'n', 't', 'i', 'c'])

print(answer)
