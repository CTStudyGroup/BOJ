import sys

input = sys.stdin.readline
N, M = map(int, input().split())


eqs = []
for _ in range(M) :
    eqs.append(list(map(int, input().split())))

def check(nums):
    """모든 변수에 값이 할당된 경우만 검사"""
    for a, b in eqs:
        ta, tb = 1, 1
        if a > 0:
            ta = nums[a]
        else:
            ta = 1 - nums[-a]
        if b > 0:
            tb = nums[b]
        else:
            tb = 1 - nums[-b]

        if ta == 0 and tb == 0:
            return False
    return True
def bt(nums, k) :
    if k == N :
        if check(nums) :
            print(1)
            sys.exit(0)
        return
    nums[k+1] = 0
    bt(nums, k+1)
    nums[k+1] = 1
    bt(nums, k + 1)

def solve() :
    num = [-1] *(N+1)
    bt(num, 0)
    
solve()
print(0)
