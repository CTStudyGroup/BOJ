import sys
input = sys.stdin.readline

def compatible(str1, str2):
    if len(str1) != len(str2):
        return False
    fwd = {}  # str1-> str2
    bwd = {}  # str2-> str1
    for a, b in zip(str1, str2):
        if a in fwd and fwd[a] != b:
            return False
        if b in bwd and bwd[b] != a:
            return False
        fwd[a] = b
        bwd[b] = a

    return True

N = int(input())
input_ = list(input().strip() for _ in range(N))
visited = [0] * N
total = 0

for start_node in range(N-1) :
        for next_node in range(start_node + 1, N) :
                if compatible( input_[next_node] ,  input_[start_node] ) :
                    visited[next_node] = 1
                    total += 1
   
print(total)

