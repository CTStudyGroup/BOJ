def rotate(t, d, state, T):
    direction = getDirection(t, d, state, T)
    for i, curr_d in enumerate(direction):
        if curr_d == 1: # clockwise
            state[i] = [state[i][-1]] + state[i][:-1]
        elif curr_d == -1: # anti-clockwise
            state[i] = state[i][1:] + [state[i][0]]
    return state

def getDirection(t, d, state, T):
    direction = [0]*T
    direction[t] = d
    for i in range(t, T-1):
        if state[i][2]!=state[i+1][6]: direction[i+1] = -direction[i]
        else: break
    for j in range(t, 0, -1):
        if state[j][6]!=state[j-1][2]: direction[j-1] = -direction[j]
        else: break
    return direction

T = int(input())
state = [list(map(int, input())) for _ in range(T)]

for _ in range(int(input())):
    t, d = list(map(int, input().split()))
    state = rotate(t-1, d, state, T)
print(sum([state[i][0] for i in range(T)]))