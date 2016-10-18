n = int(raw_input())
if n>=0 and n<=20:
    for i in xrange(0,n):
        print i**2
else:
    print 'Out of range! (0..20)'