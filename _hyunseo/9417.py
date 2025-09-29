import sys

input = sys.stdin.readline
import math

N = int(input())


def solve(nums) :
    answer = 0
    
    for i in range(len(nums) -1 ) :
        for j in range(i + 1, len(nums)) :
            answer = max(answer, math.gcd(nums[i], nums[j]))
    
    return answer

for _ in range(N) :
    numbers = list(map(int, input().split()))
    print(solve(numbers))
