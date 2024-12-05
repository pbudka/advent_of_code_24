import re

pattern = re.compile('XMAS')

def findXmas(lines):
#    print(lines)
    total = 0
    for l in lines:
        total += len(re.findall(pattern, l))
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
#    print("transposed", tlines)
    total += findXmas(tlines)
    total += findXmas(reverse(tlines))
    dlines = diagonal(lines)
    dlines += diagonal(reverse(transpose(reverse(lines))))[:-1]
#    print("diagonal",  dlines)
    total += findXmas(dlines)
    total += findXmas(reverse(dlines))
    return total

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
    print(findAllXmas(inp))
    with open("day4.txt", "r") as f:
        lines = [l[:-1] for l in f.readlines()]
        print(len(lines), len(lines[0]))
        print(lines)
        print(findAllXmas(lines))


