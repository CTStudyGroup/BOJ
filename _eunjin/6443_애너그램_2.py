import sys
input = sys.stdin.readline

N = int(input())

# 백트래킹으로 가능한 모든 문자열을 set에 넣기
def backtracking():
    global string

    if len(string) == len(word):
        print(''.join(string))
        return

    for key in cnt:
        if cnt[key]:
            string.append(key)
            cnt[key] -= 1

            backtracking()

            string.pop()
            cnt[key] += 1


for _ in range(N):
    word = sorted(list(input().strip()))  # 사전순 출력을 위해 정렬
    string = []
    cnt = {}  # 알파벳별 개수 dict

    for char in word:
        if char in cnt:
            cnt[char] += 1
        else:
            cnt[char] = 1

    backtracking()
