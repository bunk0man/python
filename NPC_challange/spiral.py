n, m = raw_input().strip().split(' ')
n = int(n)
m = int(m)

def getCol(inStringArray, ind):
    fcol = ''
    for x in xrange(len(inStringArray)):
        fcol += coded[x][ind]
    return fcol

def decodeSpiral(spiralStr,n,m):
    #spiral decoding
    i = j = spiral = start = 0
    decodedStr = ""
    while i<=m and j<=n:
        #left side
        if spiral == 0:
            temp = getCol(spiralStr, i)
            temp = temp[::-1]
            if start == 0:
                start = 1
            else:
                temp = temp[1:n]
            decodedStr += temp
            i += 1
            spiral = 1
        #top side
        elif spiral == 1:
            decodedStr += spiralStr[j][j+1:m]
            j += 1
            spiral = 2
        #right side
        elif spiral == 2:
            temp = getCol(spiralStr, m-1)
            decodedStr += temp[j:n]
            m -= 1
            spiral = 3
        #bottom side
        elif spiral == 3:
            temp = spiralStr[n-1][i:m]
            decodedStr += temp[::-1]
            n -= 1
            spiral = 0
    return decodedStr

wordCount = 0

if n>0 and m>0 and n<=20 and m<=20:
    #getting datas
    coded = ['' for x in xrange(n)]
    for x in xrange(n):
        coded[x] = str(raw_input().strip())

    words = decodeSpiral(coded,n,m)
    wordsArr = words.split("#")

    for x in xrange(len(wordsArr)):
        if wordsArr[x] != "":
            wordCount += 1

print wordCount