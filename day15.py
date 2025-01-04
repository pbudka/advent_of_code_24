def read(fname):
    movements = []
    maze = None
    with open(fname, "r") as f:
        for l in f.readlines():
            if len(l) == 1:
                maze = [list(l) for l in movements]
                movements.clear()
            movements.append(l[:-1])
    return maze, ''.join(movements)


class Wall:
    def __init__(self, x, y, maze, w=1):
        self.x = x
        self.y = y
        self.w = w
        self.maze = maze

    def move(self, x, y):
        pass

    def canMove(self):
        return False

    def getItems(self, x, y):
        items = set()
        item = self.maze.at(self.x + x, self.y + y)
        if item:
            items.add(item)
        if self.w == 2:
            item = self.maze.at(self.x + 1 + x, self.y + y)
            if item:
                items.add(item)
        return items

    def at(self, x, y):
        if self.w == 1:
            return self.y == y and self.x == x
        return self.y == y and (self.x == x or self.x + 1 == x)

    def __repr__(self):
        return f"{self.x} {self.y} {'' if self.w == 1 else 'w'}"


class Box(Wall):
    def canMove(self):
        return True

    def move(self, x, y):
        self.x += x
        self.y += y


class Robot(Box):
    def move(self, x, y):
        items = self.getAllItems(x, y)
        if items is None:
            return
        super().move(x, y)
        for it in items:
            it.move(x, y)

    def getAllItems(self, x, y):
        items = self.getItems(x, y)
        while True:
            itLen = len(items)
            for it in items:
                items = items.union(it.getItems(x, y))
            if len(items) == itLen:
                break
        for it in items:
            if not it.canMove():
                return None
        return items


class Maze:
    def __init__(self, lists=(())):
        self.furniture = set()
        self.addAll(lists)

    def add(self, item):
        self.furniture.add(item)

    def at(self, x, y):
        for item in self.furniture:
            if item.at(x, y):
                return item

    def addAll(self, lists):
        for y in range(len(lists)):
            for x in range(len(lists[0])):
                item = lists[y][x]
                if item == '#':
                    self.add(Wall(x, y, self))
                elif item == 'O':
                    self.add(Box(x, y, self))
                elif item == '@':
                    self.robot = Robot(x, y, self)
        return self

    def addAllWide(self, lists):
        for y in range(len(lists)):
            for x in range(len(lists[0])):
                item = lists[y][x]
                if item == '#':
                    self.add(Wall(x * 2, y, self, 2))
                elif item == 'O':
                    self.add(Box(x * 2, y, self, 2))
                elif item == '@':
                    self.robot = Robot(x * 2, y, self)
        return self

    def move(self, moves):
        for dir in moves:
            if dir == '^':
                self.robot.move(0, -1)
            elif dir == 'v':
                self.robot.move(0, 1)
            elif dir == '<':
                self.robot.move(-1, 0)
            elif dir == '>':
                self.robot.move(1, 0)

    def gps(self):
        gps = 0
        print(self.robot.x, self.robot.y)
        boxes = list()
        for item in self.furniture:
            if isinstance(item, Box):
                boxes.append((item.x, item.y))
                gps += item.y * 100 + item.x
        boxes.sort(key=lambda i: i[0] + i[1] * 100)
        print(boxes)
        return gps


if __name__ == '__main__':
    maze, movements = read("day15ex.txt")
    maze = Maze(maze)
    print(maze.gps())
    maze.move(movements)
    print(maze.gps())

    maze, movements = read("day15.txt")
    maze = Maze(maze)
    print(maze.gps())
    maze.move(movements)
    print(maze.gps())

    maze, movements = read("day15ex.txt")
    maze = Maze().addAllWide(maze)
    print(maze.gps())
    maze.move(movements)
    print(maze.gps())

    maze, movements = read("day15.txt")
    maze = Maze().addAllWide(maze)
    print(maze.gps())
    maze.move(movements)
    print(maze.gps())
