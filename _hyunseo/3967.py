import sys


# 조건에 맞는 지 계산하는 함수
def calculate(star) :
    if star[0] + star[2] + star[5] + star[7] != 26 :
        return False
    if star[0] + star[3] + star[6] + star[10] != 26 :
        return False
    if star[1] + star[2] + star[3] + star[4] != 26 :
        return False
    if star[1] + star[5] + star[8] + star[11] != 26 :
        return False
    if star[4] + star[6] + star[9] + star[11] != 26 :
        return False
    if star[7] + star[8] + star[9] + star[10] != 26 :
        return False
    return True

# 숫자 배열을 변환하여 정답 별을 출력하는 함수
def print_star(star) :
    for idx, val in enumerate(star) :
        star[idx] = chr(val+64)
    print(f'....{star[0]}....')
    print(f'.{star[1]}.{star[2]}.{star[3]}.{star[4]}.')
    print(f'..{star[5]}...{star[6]}..')
    print(f'.{star[7]}.{star[8]}.{star[9]}.{star[10]}.')
    print(f'....{star[11]}....')
    sys.exit()
# 백트래킹하는 함수, nxt가 비어잇는 경우, 남은 nums중 하나를 넣고
# 다음 백트래킹을 부르는 함수
def backtrack(star, nxt, nums) :
    if nxt == 12 :
        if calculate(star) :
            print_star(star)
        return
    if star[nxt] != 0 :
        backtrack(star, nxt+1, nums)
        return
    for n in list(sorted(nums)): # 여기 list
        star[nxt] = n
        nums.remove(n)
        backtrack(star, nxt + 1, nums)
        star[nxt] = 0
        nums.add(n)

star = []
nums =set(i for i in range(1, 13))
visited=set()
for _ in range(5) :
    string = input().strip()
    for s in string :
        if s == 'x' :
            star.append(0)
        if 'A' <= s <= 'L' :
            star.append(ord(s) - 64)
            nums.remove(ord(s) - 64)

backtrack(star, 0, nums)
