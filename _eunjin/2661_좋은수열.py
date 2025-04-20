N = int(input())

# 1,2,3중 하나를 선택하는데
# 걔를 선택했을 때 좋은 수열이 아니게 되면 가지치기
# 전체 길이가 N이 될때까지

# 1 ~ 길이 // 2만큼의 구간을 비교
# arr에 n을 추가했을 때 좋은수열 되는지 여부
d = [0, "1", "2", "3"]
def is_good(arr, n):
    if not arr:
        return True

    string = ''.join(map(str, arr)) + d[n]
    L = len(string)
    for l in range(1, L // 2 + 1):
        if string[L - l:] == string[L - 2 * l:L - l]:
            return False
    return True

def backtracking():
    if len(arr) == N:
        print(''.join(map(str, arr)))
        exit()

    for i in range(1, 4):
        if is_good(arr, i):
            arr.append(i)
            backtracking()
            arr.pop()

arr = []
backtracking()


