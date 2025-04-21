from itertools import combinations
N = input()

mx = 0
mn = 1e9

def recursion(string, cnt):
    global mx, mn
    # print("string:", string, ", cnt:", cnt)

    if len(string) == 1:
        mx = max(mx, cnt)
        mn = min(mn, cnt)
        return

    if len(string) == 2:
        temp = int(string[0]) + int(string[1])
        temp_str = str(temp)
        temp_cnt = cnt
        for ch in temp_str:  # 홀수 개수 세기
            if int(ch) % 2 == 1:
                temp_cnt += 1
        recursion(temp_str, temp_cnt)
    else:
        comb_list = list(combinations(range(1, len(string)), 2))  # 2개의 분할 지점 선택
        for comb in comb_list:
            st1 = string[:comb[0]]
            st2 = string[comb[0]:comb[1]]
            st3 = string[comb[1]:]

            temp = int(st1) + int(st2) + int(st3)
            temp_str = str(temp)
            temp_cnt = cnt

            for ch in temp_str:
                if int(ch) % 2 == 1:
                    temp_cnt += 1

            recursion(temp_str, temp_cnt)



cnt = 0
for ch in N:
    if int(ch) % 2 == 1:
        cnt += 1
recursion(N, cnt)

print(mn, mx)
