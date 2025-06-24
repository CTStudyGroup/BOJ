N, P, Q = map(int, input().split())

# dp
_dict = {}
_dict[0] = 1

def recursion(n):
    if n == 0:
        return 1
    p = int(n / P)
    q = int(n / Q)

    if p in _dict:
        Ap = _dict[p]
    else:
        Ap = recursion(p)
        _dict[p] = Ap

    if q in _dict:
        Aq = _dict[q]
    else:
        Aq = recursion(q)
        _dict[q] = Aq

    return Ap + Aq

print(recursion(N))
