import sys

a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))
alice = 0
bob = 0

for i in xrange(len(a)):
    if a[i] > b[i]:
        alice += 1
    if a[i] < b[i]:
        bob += 1

print alice, bob
