string = input()
arr = []

first = sum(map(int, string.split("-")[0].split("+")))

if(string.find("-") < 0):  # -가 아예 없는 경우
    result = sum(map(int, string.split("+")))
    print(result)
    exit()

result = int(first)
start = 0
while(True):
    m_idx = string.find("-", start)
    next_idx = string.find("-", m_idx+1)
    # print("m_idx:", m_idx, ", next_idx:", next_idx)
    if(next_idx == -1):
        temp = map(int, string[m_idx+1:].split("+"))
        result -= sum(temp)
        break
    else:
        temp = map(int, string[m_idx+1:next_idx].split("+"))
        result -= sum(temp)
        start = next_idx


print(result)
