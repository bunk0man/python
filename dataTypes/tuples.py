n = int(raw_input().strip())
raw = map(int, raw_input().strip().split(' '))
t = tuple(raw)
print raw, t
print hash(t)