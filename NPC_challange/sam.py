n = int(raw_input().strip())
s = map(int,raw_input().strip().split(' '))

if s[0] != 1:
    e = 1
else:
    e = 0

for x in xrange(1, len(s)):
    if (s[x]-s[x-1] != 1):
        e += 1

print e
