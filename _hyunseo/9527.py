import sys,math

sys.setrecursionlimit( 10 ** 8)
input = map(int, input().split())

def sum_f ( x) :
  if x <= 0 :
    return 0

  seung = int(math.log2(x))
  floor_2pow = 2 ** seung

  # 2, 4, 8, 16, 32 ...
  if floor_2pow == x :
    return seung*x // 2 + 1 

  diff = x - floor_2pow
  # 10 = 8 + 2
  return sum_f(floor_2pow) + diff + sum_f(diff)

a, b = map(int, input().split())
print(sum_f(b) - sum_f(a - 1))
