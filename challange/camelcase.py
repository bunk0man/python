s = raw_input().strip()
words = 0
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in xrange(len(s)):
    if s[x] in uppercase:
        words += 1
print words + 1