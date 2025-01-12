import sys

def transpose(lines):
    tlines = []
    for x in range(len(lines[0])):
        for y in range(len(lines)):
            if x == 0:
                tlines += [[lines[x][y]]]
            else:
                tlines[y] += [lines[x][y]]
    return tlines


def read(fname):
    maze = []
    with open(fname, "r") as f:
        for l in f.readlines():
            maze.append([0 if c == '#' else 1 for c in l[:-1]])

    return transpose(maze)


aLot = 200000000000000
done = dict()


def path(maze, s, e, visited, dir):
    if s == e:
        return 0
    if (s[0], s[1], dir) in done:
        return done[(s[0], s[1], dir)]
    visited.add(s)
    dirs = ">^<v"
    id = dirs.index(dir)
    r = aLot
    coords = [(s[0] + 1, s[1]), (s[0], s[1] - 1), (s[0] - 1, s[1]), (s[0], s[1] + 1)]
    addToVisited = set()
    for idx in range(len(dirs)):
        turn = abs(id - idx) % 2
        if not (turn == 0 and id != idx) and not coords[idx] in visited and maze[coords[idx][0]][coords[idx][1]]:
            vis = visited.copy()
            c = path(maze, coords[idx], e, vis, dirs[idx]) + 1 + turn * 1000
            # addToVisited.union(vis)
            if c < aLot and r < aLot:
                l = [i for i in visited]
                l.sort(key=lambda e: e[1] + e[0] * 1000)
                print("decission point", s, dir, c, r, l, coords[idx])
            if c < r:
                addToVisited = vis
                r = c
    visited.union(addToVisited)
    done[(s[0], s[1], dir)] = r
    return r


def getPath(maze):
    done.clear()
    return path(maze, (1, len(maze) - 2), (len(maze[1]) - 2, 1), set(), ">")


sys.setrecursionlimit(4000)

if __name__ == '__main__':
    maze = read("day16ex.txt")
    print(maze)
    print(getPath(maze))

    maze = read("day16ex2.txt")
    print(maze)
    print(getPath(maze))

    maze = read("day16.txt")
    print(maze)
    print(getPath(maze))
