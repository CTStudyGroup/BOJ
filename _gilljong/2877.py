from sys import stdin as s
from collections import deque
s = open('txt/2877.txt','r')

K = int(s.readline())

#홀수 > 4
#짝수 > 7
#값 // 2 짝수 -1 + 홀짝
#값 // 2 홀수 +0 + 홀짝

s = format(K+1, 'b')

s = s[1:]
print(s.replace('0', '4').replace('1', '7'))

#35분 35초