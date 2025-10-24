import sys

input = sys.stdin.readline

N, C = map(int, input().split())
w = list(map(int, input().split()))


w.sort()

def solve() :
    if C in w :
        return True
        
    for i in range(N-2):
        if w[i] >= C :
            break
        target = C - w[i] 
        j, k = i, N - 1
       
        while j < k :
            if i == j :
              total = w[k]
            else :
              total = w[j] + w[k]
            if total == target :
                return True
            elif total > target :
                k -= 1
            else :
                j += 1
    
    return False

if solve() :
    print(1)
else : 
    print(0)
