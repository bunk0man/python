import sys

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

mSum = 0
mLen = len(a)
for x in xrange(mLen):
    mSum += a[x][x] - a[x][mLen-x-1]

print abs(mSum)
