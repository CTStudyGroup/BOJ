LED = {
    0: [1,1,1,0,1,1,1],
    1: [0,0,1,0,0,0,1],
    2: [0,1,1,1,1,1,0],
    3: [0,1,1,1,0,1,1],
    4: [1,0,1,1,0,0,1],
    5: [1,1,0,1,0,1,1],
    6: [1,1,0,1,1,1,1],
    7: [0,1,1,0,0,0,1],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1]
}

def convert(n1, n2):
    global LED
    res = 0
    for i in range(7):
        res += (LED[n1][i]^LED[n2][i])
    return res

def solve(N, K, P, X):
    realNum = f"{X:0{K}d}"
    ans = 0
    for n in range(1, N+1):
        fakeNum = f"{n:0{K}d}"
        if realNum == fakeNum: continue
        total = 0
        for idx in range(K):
            total += convert(int(realNum[idx]), int(fakeNum[idx]))
            if total > P: break
        else: 
            ans+=1
    return ans

# Input
N, K, P, X = list(map(int, input().split()))
print(solve(N, K, P, X))