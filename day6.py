import re
from copy import copy


def readPuzzle(fname):
    pat = re.compile(r'#')
    with open(fname, "r") as f:
        lines = [l[:-1] for l in f.readlines()]
    i = -1
    obsCoords = set()
    pos = None
    size = (len(lines[0]), len(lines))
    for l in lines:
        i += 1
        p = 0
        if len(l) != size[0]:
            raise Exception("strange line")
        while m := pat.search(l, p):
            p = m.end()
            obsCoords.add((i, m.start()))
        if m := re.search(r'\^', l):
            if pos:
                raise Exception("pos already set")
            else:
                pos = (i, m.start())
    return obsCoords, pos, size

class Robot:
    dirs = "urdl"

    def __copy__(self):
        return Robot(copy(self.obs), self.pos, self.bounds)

    def __init__(self, obs, pos, bounds):
        self.pos = pos
        self.obs = obs
        self.dir = 0
        self.bounds = bounds

    def walk(self):
        coords = set()
        ucoords = set()
        while True:
            p = self.pos
            self.step()
            if self.obstacle():
                self.pos = p
                self.turn()
                continue
            coords.add(p)
            uc = (p[0], p[1], self.dir)
            if uc in ucoords:
                return {}
            ucoords.add(uc)
            if not self.inside():
                return coords

    def cycleObstacles(self):
        cyc = []
        for x in range(0, self.bounds[0]):
            for y in range(0, self.bounds[1]):
                obs = (x, y)
                if obs in self.obs:
                    continue
                rCopy = copy(self)
                rCopy.obs.add(obs)
                if len(rCopy.walk()) == 0:
                    cyc.append(obs)
        return cyc

    def obstacle(self):
        return self.pos in self.obs

    def inside(self):
        return 0 <= self.pos[0] < self.bounds[0] and 0 <= self.pos[1] < self.bounds[1]

    def turn(self):
        self.dir = (self.dir + 1) % 4

    def step(self):
        if self.dirs[self.dir] == "u":
            self.pos = (self.pos[0]-1, self.pos[1])
        elif self.dirs[self.dir] == "r":
            self.pos = (self.pos[0], self.pos[1]+1)
        elif self.dirs[self.dir] == "d":
            self.pos = (self.pos[0]+1, self.pos[1])
        else:  # "l"
            self.pos = (self.pos[0], self.pos[1]-1)


if __name__ == '__main__':
    r = Robot(*readPuzzle("day6ex.txt"))
    r2 = copy(r)
    print(len(r.walk()))
    o = r2.cycleObstacles()
    print(o)
    print(len(o))

    r = Robot(*readPuzzle("day6.txt"))
    r2 = copy(r)
    print(len(r.walk()))
    o = r2.cycleObstacles()
    print(o)
    print(len(o))
