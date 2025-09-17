import collections

while True:
    try:
        flag = True
        x = int(input()) * 10**7
        n = int(input().strip())
        lego = collections.defaultdict(int)
        inputs = []

        for _ in range(n):
            val = int(input().strip())
            inputs.append(val)
            lego[val] += 1   # 개수 카운트

        inputs.sort()

        for val in inputs:
            need = x - val
            if need in lego:
                if need != val and lego[need] > 0:
                    print(f'yes {val} {need}')
                    flag = False
                    break
                elif need == val and lego[val] > 1:
                    print(f'yes {val} {need}')
                    flag = False
                    break

        if flag:
            print('danger')

    except:
        break
