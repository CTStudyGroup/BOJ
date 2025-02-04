T = int(input())

calc = [" ", "+", "-"]


def dfs(N, num, string):
    global answer_list
    if num == N:
        answer = eval(string.replace(' ', ''))
        if answer == 0:
            answer_list.append(string)
        return
    else:
        next_num = num+1
        for i in range(3):
            dfs(N, next_num, string+calc[i]+str(next_num))


for _ in range(T):
    N = int(input())
    answer_list = []
    dfs(N, 1, "1")
    for ans in answer_list:
        print(ans)
    print()
