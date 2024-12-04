import re

pattern = re.compile('(\\d+)\\W+(\\d+)')

def readInput(fname):
    list1 = []
    list2 = []
    with open(fname, "r") as f:
        for l in f:
            m = pattern.match(l)
            list1.append(int(m.group(1)))
            list2.append(int(m.group(2)))
    return list1, list2

def distance(list1, list2):
    list1s = sorted(list1)
    list2s = sorted(list2)
    sum = 0
    for i in range(len(list1)):
        sum += abs(list1s[i] - list2s[i])
    return sum


(list1, list2) = readInput("day1.txt")
print(distance(list1, list2))