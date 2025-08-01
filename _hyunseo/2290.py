s, n = map(int, input().split())
n = str(n)

h, v = '-', '|'


def construct_segment(n):
    lcd = [[' '] * (s + 2) for _ in range(2 * s + 3)]
    for i in range(1, s + 1):

        # a
        if n in '02356789':
            lcd[0][i] = h

        # b
        if n in '01234789':
            lcd[i][-1] = v

        # c
        if n in '013456789':
            lcd[s + 1 + i][-1] = v

        # d
        if n in '0235689':
            lcd[2 * s + 2][i] = h
            # lcd[-1][i] = h도 가능

        # e
        if n in '0268':
            lcd[s + 1 + i][0] = v

        # f
        if n in '045689':
            lcd[i][0] = v

        # g
        if n in '2345689':
            lcd[s + 1][i] = h

    return lcd


display = [construct_segment(i) for i in n]

for line in zip(*display):
    for r in line:
        print(''.join(r), end=' ')
    print()  # 필수: 한 행이 끝나면 줄바꿈
