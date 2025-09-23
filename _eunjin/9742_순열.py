import sys
input = sys.stdin.readline

def backtracking(k):
    global x, found
    if found:
        return

    if k == len(string):
        if x == N:
            print(string, N, "=", ''.join(map(str, arr)))
            found = True
            return
        x += 1

    for i in range(len(string)):
        if not visited[i]:
            visited[i] = True
            arr.append(string[i])
            backtracking(k + 1)
            arr.pop()
            visited[i] = False


while True:
    try:
        string, N = input().split()
        N = int(N)
        x = 1
        visited = [False] * len(string)
        found = False
        arr = []
        backtracking(0)
        if not found:
            print(string, N, "=", "No permutation")
    except:
        break
