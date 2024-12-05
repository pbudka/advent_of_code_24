import re

pattern = re.compile('XMAS')
pattern2 = re.compile('MAS')


def findXmas(lines):
#    print(lines)
    total = 0
    for l in lines:
        total += len(re.findall(pattern, l))
    print(total)
    return total


def findMas(lines):
    #    print(lines)
    total = 0
    for l in lines:
        total += len(re.findall(pattern2, l))
    print(total)
    return total


def reverse(lines):
    rlines = []
    for x in lines:
        xl = list(x)
        xl.reverse()
        rlines.append("".join(xl))
    return rlines

def transpose(lines):
    tlines = []
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if x == 0:
                tlines.append("".join(lines[x][y]))
            else:
                tlines[y] += lines[x][y]
    return tlines

def diagonal(lines):
    dlines = []
    for y in range(len(lines)):
        cy = y
        str = ''
        for x in range(len(lines[0])):
            str += lines[cy][x]
            cy -= 1
            if cy < 0:
                dlines.append(str)
                break
    return dlines

def findAllXmas(lines):
    total = 0
    total += findXmas(lines)
    total += findXmas(reverse(lines))
    tlines = transpose(lines)
    print("transposed", tlines)
    total += findXmas(tlines)
    total += findXmas(reverse(tlines))
    dlines = diagonal(lines)
    dlines += diagonal(reverse(transpose(reverse(lines))))[:-1]
    print("diagonal1",  dlines)
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    dlines = diagonal(reverse(lines))
    dlines += diagonal(reverse(transpose(lines)))[:-1]
    print("diagonal2",  dlines)
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    return total

def conversionTable(size):
    list = [[(y,x) for x in range(size)] for y in range(size)]
    return list

tdiagonal1 = []
tdiagonal2 = []

def findAllMas(lines):
    global tdiagonal1, tdiagonal2
    conv = conversionTable(len(lines))
    tdiagonal1 = diagonal(conv)
    tdiagonal1 += reversed(diagonal(reverse(transpose(reverse(conv))))[:-1])
    print(tdiagonal1)
    tdiagonal2 = diagonal(reverse(conv))
    tdiagonal2 += reversed(diagonal(reverse(transpose(conv)))[:-1])
    print(tdiagonal1)
    total = 0
    dlines = diagonal(lines)
    dlines += reversed(diagonal(reverse(transpose(reverse(lines))))[:-1])
    print("diagonal1",  dlines)
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    dlines = diagonal(reverse(lines))
    dlines += reversed(diagonal(reverse(transpose(lines)))[:-1])
    print("diagonal2",  dlines)
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    return total

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
#    print(findAllXmas(inp))
    print(findAllMas(inp))
#    print(findAllXmas(readLines("day4.txt")))
print(conversionTable(4))


