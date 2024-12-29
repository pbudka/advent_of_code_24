import re

cost = {'a': 3, 'b': 1}


# a*ax + b*bx = x
# a*ay + b*by = y
# a = (x-b*bx)/ax
# ay*x/ax - ay*b*bx/ax + b*by = y
# ay*x/ax - b*(ay*bx/ax - by) = y
# b=(ay*x/ax - y) / (ay*bx/ax - by)
def getResult(ax, ay, bx, by, x, y):
    b = (ay * x / ax - y) / (ay * bx / ax - by)
    a = (x - b * bx) / ax
    a = round(a, 3)
    b = round(b, 3)
    if a == int(a) and b == int(b) and x == a * ax + b * bx and y == a * ay + b * by:
        return a * cost['a'] + b * cost['b']
    return 0


def read(fname, add=0):
    delta = re.compile(r'Button ([AB]).*X\+(\d+).*Y\+(\d+)')
    result = re.compile(r'Prize.*X=(\d+).*Y=(\d+)')
    inputs = []
    with open(fname, "r") as f:
        for l in f.readlines():
            if len(l) > 1:
                if m := re.search(delta, l):
                    if m.group(1) == 'A':
                        ret = [int(m.group(2)), int(m.group(3))]
                    else:
                        ret += [int(m.group(2)), int(m.group(3))]
                if m := re.search(result, l):
                    ret += [int(m.group(1)) + add, int(m.group(2)) + add]
                    inputs.append(ret)
    return inputs


if __name__ == '__main__':
    inp = read("day13ex.txt")
    print(sum([getResult(*i) for i in inp]))

    inp = read("day13.txt")
    print(sum([getResult(*i) for i in inp]))

    inp = read("day13ex.txt", 10000000000000)
    print(sum([getResult(*i) for i in inp]))

    inp = read("day13.txt", 10000000000000)
    print(sum([getResult(*i) for i in inp]))
