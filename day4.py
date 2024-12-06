import re

pattern = re.compile('XMAS')
pattern2 = re.compile('MAS')


def findXmas(lines):
    slines = toString(lines)
    print(slines)
    total = 0
    for l in slines:
        total += len(re.findall(pattern, l))
    print(total)
    return total


def findMas(lines):
    slines = toString(lines)
    hitCoords = []
    i = 0
    for l in slines:
        if m := re.search(pattern2, l):
            hitCoords += [(i, m.span()[0]+1)]
        i += 1
    return hitCoords

def toList(lines):
    return [list(l) for l in lines]

def toString(lines):
    return [''.join(l) for l in lines]

def clone(lines):
    return [l[:] for l in lines]

def reverse(lines):
    rlines = clone(lines)
    return [list(reversed(l)) for l in rlines]

def transpose(lines):
    tlines = []
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if x == 0:
                tlines += [[lines[x][y]]]
            else:
                tlines[y] += [lines[x][y]]
    return tlines

def diagonal(lines):
    dlines = []
    for y in range(len(lines)):
        cy = y
        lst = []
        for x in range(len(lines[0])):
            lst += [lines[cy][x]]
            cy -= 1
            if cy < 0:
                dlines += [lst]
                break
    return dlines

def findAllXmas(lines):
    total = 0
    total += findXmas(lines)
    total += findXmas(reverse(lines))
    tlines = transpose(lines)
    print("transposed", toString(tlines))
    total += findXmas(tlines)
    total += findXmas(reverse(tlines))
    dlines = diagonal(lines)
    dlines += diagonal(reverse(transpose(reverse(lines))))[:-1]
    print("diagonal1",  toString(dlines))
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    dlines = diagonal(reverse(lines))
    dlines += diagonal(reverse(transpose(lines)))[:-1]
    print("diagonal2",  toString(dlines))
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    return total

def conversionTable(size):
    list = [[(y,x) for x in range(size)] for y in range(size)]
    return list

def findAllMas(lines):
    conv = conversionTable(len(lines))

    convTab = diagonal(conv)
    convTab += reversed(diagonal(reverse(transpose(reverse(conv))))[:-1])
#    print("diag conf table 1 ", convTab)
    dlines = diagonal(lines)
    dlines += reversed(diagonal(reverse(transpose(reverse(lines))))[:-1])
#    print("diagonal1",  toString(dlines))
    hits = findMasHits(convTab, dlines)

    convTab = diagonal(reverse(conv))
    convTab += reversed(diagonal(reverse(transpose(conv)))[:-1])
#    print("diag conf table 1 ", convTab)
    dlines = diagonal(reverse(lines))
    dlines += reversed(diagonal(reverse(transpose(lines)))[:-1])
#    print("diagonal2",  toString(dlines))
    hits2 = findMasHits(convTab, dlines)

    hits = hits2.intersection(hits)
    hits = list(hits)
    hits.sort()
    print("intersection", hits)
    return len(hits)


def findMasHits(convTab, dlines):
    hits = findMas(dlines)
    convHits = {convTab[c[0]][c[1]] for c in hits}
    convTab = reverse(convTab)
    hits = findMas(reverse(dlines))
    convHits = convHits.union({convTab[c[0]][c[1]] for c in hits})
    return convHits


def readLines(fname):
    with open(fname, "r") as f:
        lines = [l[:-1] for l in f.readlines()]
    print(len(lines), len(lines[0]))
    print(lines)
    return lines


if __name__ == '__main__':
    inp = ["MMMSXXMASM",
           "MSAMXMSMSA",
           "AMXSXMAAMM",
           "MSAMASMSMX",
           "XMASAMXAMM",
           "XXAMMXXAMA",
           "SMSMSASXSS",
           "SAXAMASAAA",
           "MAMMMXMMMM",
           "MXMXAXMASX"]
    print("findAllXmas: ", findAllXmas(inp))
    print("findAllMas: ", findAllMas(inp))
    print("findAllXmas: ", findAllXmas(readLines("day4.txt")))
    print("findAllMas: ", findAllMas(readLines("day4.txt")))


