
def read(fname):
    ret = []
    with open(fname, "r") as f:
        for l in f.readlines():
            ret.append([int(i) for i in l[:-1]])
    return ret

class Score:
    def __init__(s, data):
        s.data = data
        s.maxX = len(s.data[0])
        s.maxY = len(s.data)

    def scoreHead(s, x, y, found):
        find = s.data[x][y] + 1
        if find > 9:
            if (x,y) in found:
                return 1 # return 0 to count how many 9s can be reached from 0
            found.add((x,y))
            return 1
        score = 0
        if x-1 >= 0 and s.data[x-1][y] == find:
            score += s.scoreHead(x-1, y, found)
        if x+1 < s.maxX and s.data[x + 1][y] == find:
            score += s.scoreHead(x+1, y, found)
        if y-1 >= 0 and s.data[x][y-1] == find:
            score += s.scoreHead(x, y-1, found)
        if y+1 < s.maxY and s.data[x][y + 1] == find:
            score += s.scoreHead(x, y+1, found)
        return score

    def scoreHeads(s):
        scores = []
        for x in range(len(s.data[0])):
            for y in range(len(s.data)):
                if not s.data[x][y]:
                    scores.append((x, y, s.scoreHead(x, y, set())))
        return scores

if __name__ == '__main__':
    data = read("day10ex.txt")
    print(data)
    score = Score(data).scoreHeads()
    print(score)
    print(sum([x[2] for x in score]))

    data = read("day10.txt")
    print(data)
    score = Score(data).scoreHeads()
    print(score)
    print(sum([x[2] for x in score]))

