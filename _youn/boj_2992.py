from itertools import permutations

def pToVal(p):
    val = 0
    for i in range(len(p)):
        val += (p[i]*(10**(len(p)-i-1)))
    return val

def bigSmallVal(X):
    X_list = sorted(list(map(int, str(X))))
    ans = 2e20
    per = filter(lambda p: sorted(list(p))==X_list, permutations(X_list, len(X_list)))
    for p in per:
        pVal = pToVal(p)
        if p[0]!= 0 and X < pVal:
            ans = min(ans, pVal)
    return ans if ans!=2e20 else 0

X = int(input())
print(bigSmallVal(X))

