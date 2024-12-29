import re


class Robot:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __repr__(self):
        return f"({self.x},{self.y})"  # ({self.dx},{self.dy})"

    def move(self, x, y):
        self.x += self.dx
        self.y += self.dy
        if self.x < 0:
            self.x += x
        if self.y < 0:
            self.y += y
        if self.x >= x:
            self.x -= x
        if self.y >= y:
            self.y -= y

    def inside(self, fx, tx, fy, ty):
        return fx <= self.x < tx and fy <= self.y < ty


def read(fname):
    robot = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    robots = []
    with open(fname, "r") as f:
        for l in f.readlines():
            if len(l) > 1:
                if m := re.search(robot, l):
                    robots.append(Robot(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))))
    return robots


def move(robots, n, x, y):
    for i in range(n):
        for r in robots:
            r.move(x, y)


def count(robots, x, y):
    xh = x // 2
    yh = y // 2
    print(xh, yh)
    c1 = [r for r in robots if r.inside(0, xh, 0, yh)]
    c2 = [r for r in robots if r.inside(0, xh, yh + 1, y)]
    c3 = [r for r in robots if r.inside(xh + 1, x, 0, yh)]
    c4 = [r for r in robots if r.inside(xh + 1, x, yh + 1, y)]
    print(c1, c2, c3, c4, len(robots))
    return len(c1) * len(c2) * len(c3) * len(c4)


if __name__ == '__main__':
    robots = read("day14ex.txt")
    print(robots)
    move(robots, 100, 11, 7)
    print(robots)
    print(count(robots, 11, 7))

    robots = read("day14.txt")
    print(robots)
    move(robots, 100, 101, 103)
    print(robots)
    print(count(robots, 101, 103))
