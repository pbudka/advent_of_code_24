def uncompress(data):
    file = True
    result = []
    id = 0
    for ch in data:
        if file:
            result += [id]*int(ch)
            id += 1
        else:
            result += [None]*int(ch)
        file = not file
    return result

def move(data):
    p = data.index(None)
    for i in range(len(data)-1, -1, -1):
        if data[i] is not None:
            if p >= i:
                return
            data[p] = data[i]
            data[i] = None
            p = data.index(None, p)

def checksum(data):
    s = 0
    for i in range(0,data.index(None)):
        s += i * data[i]
    return s

def read(fname):
    with open(fname, "r") as f:
        return f.readline()[:-1]


if __name__ == '__main__':
    data = uncompress("2333133121414131402")
    print(data)
    move(data)
    print(data)
    print(checksum(data))

    data = read("day9.txt")
    data = uncompress(data)
    print(data)
    move(data)
    print(data)
    print(checksum(data))
