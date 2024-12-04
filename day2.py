import re

pattern = re.compile('(\\d+)\\W+(\\d+)\\W+(\\d+)\\W+(\\d+)\\W+(\\d+)\\W+(\\d+)\\W+(\\d+)')


def readInput(fname):
    reports = []
    with open(fname, "r") as f:
        for l in f:
            levels = []
            for n in l.split(" "):
                levels.append(int(n))
            reports.append(levels)

    return reports

def isSafe(level, inc):
    pn = -1
    for n in level:
        if pn != -1:
            d = n - pn if inc else pn - n
            if d < 1 or d > 3:
                    return False
        pn = n
    return True

def isSafeTolerant(level):
    if isSafe(level, level[1] > level[0]):
        return True
    for i in range(len(level)):
        l2 = level[:]
        del l2[i]
        if isSafe(l2, l2[1] > l2[0]):
            # print("after deleting ", i, level[i])
            return True


def safeLevels(reports):
    safe = 0
    for r in reports:
        if isSafe(r, r[1] > r[0]):
            safe += 1
    return safe

def safeLevelsWithTolerance(reports):
    safe = 0
    for r in reports:
        if (isSafeTolerant(r)):
            safe += 1
        # print(r, safe)
    return safe


if __name__ == '__main__':
    test = [[7,6,4,2,1],
    [1,2,7,8,9],
    [9,7,6,2,1],
    [1,3,2,4,5],
    [8,6,4,4,1],
    [1,3,6,7,9]]
    print(safeLevelsWithTolerance(test))
    
    reports = readInput("day2.txt")
    print(safeLevels(reports))
    print(safeLevelsWithTolerance(reports))
