
def solve(S:str):
    while True:
        idx = S.find('()')
        if idx == -1: return len(S)
        S = S[:idx] + S[idx+2:]
        print(S)

S = input()
print(solve(S))