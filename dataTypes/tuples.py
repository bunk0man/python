n = int(raw_input().strip())
t = tuple(map(int, raw_input().strip().split(' ')))
print hash(t)