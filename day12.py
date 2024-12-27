def read(fname):
    ret = []
    with open(fname, "r") as f:
        for l in f.readlines():
            ret.append(list(l[:-1]))
    return ret


explored = set()


class Garden:
    def __init__(self, data, i, j):
        self.coords = set()
        self.been = set()
        self.letter = data[i][j]
        self.data = data
        self.h = len(data)
        self.w = len(data[0])
        self.explore(i, j)

    def explore(self, i, j):
        self.been.add((i, j))
        if (i, j) not in explored and self.data[i][j] == self.letter:
            explored.add((i, j))
            self.coords.add((i, j))
            if self.check(i + 1, j): self.explore(i + 1, j)
            if self.check(i - 1, j): self.explore(i - 1, j)
            if self.check(i, j + 1): self.explore(i, j + 1)
            if self.check(i, j - 1): self.explore(i, j - 1)

    def check(self, i, j):
        return 0 <= i < self.h and 0 <= j < self.w and (i, j) not in self.been and (i, j) not in explored

    def __repr__(self):
        return f"G{self.letter} {len(self.coords)}x{self.perimeter()}"

    def perimeter(self):
        per = 0
        for (i, j) in self.coords:
            if (i - 1, j) not in self.coords: per += 1
            if (i + 1, j) not in self.coords: per += 1
            if (i, j - 1) not in self.coords: per += 1
            if (i, j + 1) not in self.coords: per += 1
        return per

    def perimeter2(self):
        edgeCoords = {'u': set(), 'd': set(), 'l': set(), 'r': set()}
        for (i, j) in self.coords:
            if (i - 1, j) not in self.coords: edgeCoords['u'].add((i, j))
            if (i + 1, j) not in self.coords: edgeCoords['d'].add((i, j))
            if (i, j - 1) not in self.coords: edgeCoords['l'].add((i, j))
            if (i, j + 1) not in self.coords: edgeCoords['r'].add((i, j))
        for d, crds in edgeCoords.items():
            sort = 0 if d in 'ud' else 1
            other = 0 if sort else 1
            prev = (-10, -10)
            for el in sorted(crds, key=lambda l: l[sort] * 10000 + l[other]):
                if el[sort] == prev[sort] and el[other] - prev[other] == 1:
                    crds.remove(el)
                prev = el
        return sum([len(x) for x in edgeCoords.values()])


def regions(data):
    h = len(data)
    w = len(data[0])
    explored.clear()
    regs = list()
    for i in range(0, h):
        for j in range(0, w):
            if (i, j) not in explored:
                g = Garden(data, i, j)
                regs.append(g)
    return regs


def cost(regions):
    cost = 0
    for r in regions:
        cost += len(r.coords) * r.perimeter()
    return cost


def cost2(regions):
    cost = 0
    for r in regions:
        cost += len(r.coords) * r.perimeter2()
    return cost


if __name__ == '__main__':
    data = read("day12ex.txt")
    print(data)
    regs = regions(data)
    print(len(data) * len(data[0]), sum([len(c.coords) for c in regs]))
    print(cost(regs), cost2(regs), len(explored), regs)

    data = read("day12.txt")
    # print(data)
    regs = regions(data)
    print(len(data) * len(data[0]), sum([len(c.coords) for c in regs]))
    print(cost(regs), cost2(regs), len(explored), regs)
