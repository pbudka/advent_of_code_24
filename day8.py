def read(fname):
    a = dict()
    bounds = None
    with open(fname, "r") as f:
        y = 0
        for l in f.readlines():
            x = 0
            for ch in l[:-1]:
                if ch != '.':
                    if not ch in a:
                        a[ch] = set()
                    a[ch].add((x, y))
                x += 1
            y += 1
        else:
            bounds = (x, y)

    return a, bounds

def shadows(antenas, bounds):
    shadows = set()
    for a in antenas:
        for aa in antenas:
            if a is aa:
                continue
            s = (a[0]-aa[0], a[1]-aa[1])
            if 0 <= s[0] < bounds[0] and 0 <= s[1] < bounds[1]:
                shadows.add(s)
            s = (aa[0]-a[0], aa[1]-a[1])
            if 0 <= s[0] < bounds[0] and 0 <= s[1] < bounds[1]:
                shadows.add(s)
    return shadows


if __name__ == '__main__':
    (antenas, bounds) = read("day8ex.txt")
    for a, ant in antenas.items():
        print(a)
        print(shadows(ant, bounds))

