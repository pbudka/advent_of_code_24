def read(fname):
    antenas = dict()
    with open(fname, "r") as f:
        y = 0
        for l in f.readlines():
            x = 0
            for ch in l[:-1]:
                if ch != '.':
                    if not ch in antenas:
                        antenas[ch] = set()
                    antenas[ch].add((x, y))
                x += 1
            y += 1
        else:
            bounds = (x, y)

    return antenas, bounds

def shadows(antenas, bounds):
    shadows = set()
    for a in antenas:
        for b in antenas:
            if b is a:
                continue
            s = (2*a[0]-b[0], 2*a[1]-b[1])
            if 0 <= s[0] < bounds[0] and 0 <= s[1] < bounds[1]:
                shadows.add(s)
            s = (2*b[0]-a[0], 2*b[1]-a[1])
            if 0 <= s[0] < bounds[0] and 0 <= s[1] < bounds[1]:
                shadows.add(s)
    return shadows


def allShadows(antenas, bounds):
    shadows = set()
    for a in antenas:
        for b in antenas:
            if b is a:
                continue
            addShadows((a[0], a[1]), (a[0] - b[0], a[1] - b[1]), bounds, shadows)
            addShadows((a[0], a[1]), (b[0] - a[0], b[1] - a[1]), bounds, shadows)
    return shadows

def addShadows(start, delta, bounds, shadows):
    while True:
        shadows.add(start)
        start = (start[0] + delta[0], start[1] + delta[1])
        if not (0 <= start[0] < bounds[0] and 0 <= start[1] < bounds[1]):
            break


if __name__ == '__main__':
    (antenas, bounds) = read("day8ex.txt")
    print(antenas, bounds)
    allSh = set()
    for a, ant in antenas.items():
        print(a)
        sh = allShadows(ant, bounds)  # shadows()
        allSh = allSh.union(sh)
        print(sh, len(sh))
    print(allSh, len(allSh))

    (antenas, bounds) = read("day8.txt")
    print(antenas, bounds)
    allSh = set()
    for a, ant in antenas.items():
        print(a)
        sh = allShadows(ant, bounds)  # shadows()
        allSh = allSh.union(sh)
        print(sh, len(sh))
    print(allSh, len(allSh))