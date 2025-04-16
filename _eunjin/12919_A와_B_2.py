from collections import deque

S = input()
T = input()

q = deque(S)


# A
# AB -> BA
# BAB -> BAB
# BABA

# A 추가
# reverse = True 이면 queue의 앞에 A 추가
# reverse = False 이면 queue의 뒤에 A 추가

# B 추가
# reverse = True 이면 queue의 앞에 B 추가, reverse = False로 변경
# reverse = False 이면 queue의 뒤에 B 추가, reverse = True로 변경

reverse = False

while len(q) < len(T)
