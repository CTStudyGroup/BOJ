# 공백이 사라진 수열
num_without_space = input()

# N 구하기
L = len(num_without_space)
N = L if L<=9 else (L-9)//2 + 9

# 이 수열은 1 ~ N까지로 이루어져있고, 공백으로 분리되어 있음
# 만든 순열은 1, 2, 3, ... , N을 포함해야 함.

def backtrack(path, idx) :
    # 종료 조건
    if idx == len(num_without_space):
        print(*path)
        exit()
        
    # 후보군 탐색
    for next_num_len in range(1, 3) :  # N은 50 이하, 한자릿수or두자릿수
        if idx + next_num_len > len(num_without_space) :continue
        next_num = int(''.join(num_without_space[idx:idx + next_num_len]))
        if next_num not in path and next_num <= N :
            path.append(next_num)
            backtrack(path, idx + next_num_len)
            path.pop()

backtrack([], 0)
