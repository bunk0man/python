num = int(raw_input().strip())
a = tuple(map(int, raw_input().strip().split(' ')))
p = n = z = float(0)

for i in xrange(num):
    if a[i] > 0:
        p += 1
    elif a[i] < 0:
        n += 1
    else:
        z += 1

print '%.6f' % (p/num), '\n%.6f' % (n/num), '\n%.6f' % (z/num)