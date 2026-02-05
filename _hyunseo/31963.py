
import sys, math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))


answer = 0 
current_k = 0


for i in range(N-1) :
    prev = arr[i]
    curr = arr[i + 1 ]
    
    if prev > curr :
        count = 0
        while curr < prev :
            curr *= 2
            count += 1
        current_k += count
    
    if past <= arr[n+1] : 
        past = arr[n+1]
        continue
    else :
        count = 0

        while prev * 2 <= curr :
            prev *= 2
            count += 1
        current_k = max(0, current_k - count) 
    answer += current_k
print(answer)
