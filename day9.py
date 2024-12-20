import re

def uncompress(data):
    file = True
    result = []
    fid = 0
    for ch in data:
        if file:
            result += [fid]*int(ch)
            fid = (fid + 1)
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

def replaceAtIndex(text, index, replacement):
    return text[:index] + replacement + text[index + len(replacement):]

def moveWholeString(data):
    string = ''.join(['.' if i is None else str(i) for i in data])
    print(string)
    digit = re.compile(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)')
    i = 0
    for word in list(re.finditer(digit, string))[::-1]:
        i += 1
        if i % 1 == 0:
            print(string[0:200], i, word.start(), word.group(0))
        if i > 20:
            return  string
        wordLen = word.end() - word.start()
        space = re.search(r'[.]{' + str(wordLen) + r',}', string[0:word.start()])
        if space:
            string = (string[:space.start()] +
                      word.group(0) +
                      string[space.start() + wordLen:word.start()] +
                      '.' * wordLen +
                      string[word.start() + wordLen:])
    print(string)
    return string

def moveWhole(data):
    ### replace regex with a search in a list
    string = ''.join(['.' if i is None else str(i) for i in data])
    print(string)
    digit = re.compile(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)')
    i = 0
    for word in list(re.finditer(digit, string))[::-1]:
        i += 1
        if i % 1 == 0:
            print(string[0:200], i, word.start(), word.group(0))
        if i > 20:
            return  string
        wordLen = word.end() - word.start()
        space = re.search(r'[.]{' + str(wordLen) + r',}', string[0:word.start()])
        if space:
            string = (string[:space.start()] +
                      word.group(0) +
                      string[space.start() + wordLen:word.start()] +
                      '.' * wordLen +
                      string[word.start() + wordLen:])
    print(string)
    return string




def checksum(data):
    s = 0
    for i in range(0, data.index(None)):
        s += i * data[i]
    return s

def checksum2(data):
    s = 0
    for i in range(0, len(data)):
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
#    print(data)
    move(data)
#    print(data)
    print(checksum(data))

    data = uncompress("2333133121414131402")
    print(data)
    data = moveWhole(data)
    print(data)
    print(checksum2([int(i) if i != '.' else 0 for i in data]))

    data = uncompress("233313312141413140225")
    print(data)

    data = read("day9.txt")
    data = uncompress(data)
#    data = moveWhole(data)
#    print(checksum2([int(i) if i != '.' else 0 for i in data]))
    print(90546720886)
