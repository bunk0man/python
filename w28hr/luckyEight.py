import sys

def genNums(array, chars):
    temp = ""
    for k in array:
        temp += chars[k]
    return temp

def genShuffle(indexes,limits,numCharacters):
    numShuffles = []
    j = len(indexes)-1
    while indexes!=limits and j>=0:
        numShuffles.append(genNums(indexes, numCharacters))
        if indexes[j]==limits[j]:
            j -= 1
        indexes[j] += 1
    numShuffles.append(genNums(indexes, numCharacters))
    return numShuffles

def generateIndexes(numArray, db):
    res = []
    iArray = []
    nArray = []
    for i in range(db):
        iArray.append(i)
        nArray.insert(0, db-i-1)
        res += genShuffle(iArray[:], nArray[:], numArray)
        print(res)
    return res

def luckyEight(numbers):
    counter=0
    for element in numbers:
        if int(element)%8==0 :
            counter+=1
    return counter

n = int(input().strip())
number = input().strip()
number = list(number)

resNum = generateIndexes(number, n)
bigRes = luckyEight(resNum) % ( 10**9 + 7 )
print(resNum, bigRes)
