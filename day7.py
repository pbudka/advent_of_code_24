def read(fname):
    a = dict()
    with open(fname, "r") as f:
        for l in f.readlines():
            s = l.split(':')
            a[int(s[0])] = [int(x) for x in s[1].split(" ") if len(x)]
    return a


def assertTwoOp(exp, vals):
    dvals = {i-1: vals[i] for i in range(0, len(vals))}
    act = 0
    for mask in range(0, pow(2, len(vals) - 1)):
        for i, v in dvals.items():
            if i == -1:
                act = v
            elif mask & (1 << i):
                act *= v
            else:
                act += v
        if act == exp:
            return True
    return False

def assertThreeOp(exp, vals):
    dvals = {i-1: vals[i] for i in range(0, len(vals))}
    act = 0
    for mask in range(0, pow(3, len(vals) - 1)):
        rmask = reversedMaskString(mask)
        for i, v in dvals.items():
            if i == -1:
                act = v
                continue
            digit = int(rmask[i])
            if digit == 0:
                act *= v
            elif digit == 1:
                act += v
            else:  # concatenate
                act = int(str(act) + str(v))
        if act == exp:
            return True
    return False


def reversedMaskString(mask):
    rmask = to_radix(3, mask)
    rmask = list(rmask)
    rmask.reverse()
    rmask = "".join(rmask) + '000000000000000000000000000000000000000000000000000000'
    return rmask


def to_radix(radix, n):
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = str(n % radix) + result
        n //= radix
    return result


if __name__ == '__main__':


    ass = read("day7ex.txt")
    tot = 0
    for exp, vals in ass.items():
        if assertTwoOp(exp, vals):
            tot += exp
    print(tot)

    ass = read("day7ex.txt")
    tot = 0
    for exp, vals in ass.items():
        if assertThreeOp(exp, vals):
            tot += exp
    print(tot)

    ass = read("day7.txt")
    tot = 0
    for exp, vals in ass.items():
        if assertTwoOp(exp, vals):
            tot += exp
    print(tot)

    ass = read("day7.txt")
    tot = 0
    for exp, vals in ass.items():
        if assertThreeOp(exp, vals):
            tot += exp
    print(tot)

