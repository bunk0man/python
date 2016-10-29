import sys

n = int(raw_input().strip())

for x in xrange(n):
    for j in xrange(n):
        if j < (n-x-1):
            sys.stdout.write(' ')
        else:
            sys.stdout.write('#')
    sys.stdout.write('\n')