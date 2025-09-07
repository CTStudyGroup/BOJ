# 문자열에서 가장 최소값을 찾고 -> 그 뒤에 있는 애들을 모두 출력한다.
# 위의 것을 반복한다. (찾은 문자열의 최소 값이 index 0일 경우까지 반복)

zoac = list(input().strip())
switch = [0] * len(zoac)


def find_minimum(from_index, to_index):
    sub_string = zoac[from_index:to_index+1]
    minimum = min(sub_string)
    minimum_index = sub_string.index(minimum)+from_index
    switch[minimum_index] = 1

    printing = []
    for i in range(len(switch)):
        if(switch[i] == 1):
            printing.append(zoac[i])

    print("".join(printing))

    if(from_index == to_index):
        return

    if(minimum_index < to_index):
        find_minimum(minimum_index+1, to_index)

    if(minimum_index > from_index):
        find_minimum(from_index, minimum_index-1)

start = 0
end = len(zoac) - 1

find_minimum(start, end)