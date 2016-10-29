aList = command = []

n = int(raw_input().strip())

for i in xrange(n):
    command = map(str, raw_input().strip().split(' '))
    if command[0] == "insert":
        aList.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
        print aList
    elif command[0] == "remove":
        aList.remove(int(command[1]))
    elif command[0] == "append":
        aList.append(int(command[1]))
    elif command[0] == "sort":
        aList.sort()
    elif command[0] == "pop":
        aList.pop()
    elif command[0] == "reverse":
        aList.reverse()
