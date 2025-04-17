S = list(input())
T = list(input())

def dfs(t):
    if t == S:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':  # 마지막이 A이면
        dfs(t[:-1])  # 제거해서 재귀
    if t[0] == 'B':  # 처음이 B이면
        dfs(t[1:][::-1])  # B제거하고, 뒤집어서 재귀
dfs(T)
print(0)
