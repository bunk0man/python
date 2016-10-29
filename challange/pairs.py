import sys

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

i=db=0
c.sort()
if len(c) > 1:
    while i < len(c)-1:
        if c[i] == c[i+1]:
            db += 1
            # print c[i], c[i+1]
            i += 2
        else:
            i += 1
print db