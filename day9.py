import re

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

def replaceAtIndex(text, index, replacement):
    return text[:index] + replacement + text[index + len(replacement):]

def moveWhole(data):
    string = ''.join(['.' if i is None else str(i) for i in data])
    digit = re.compile(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)')
    subStr = string[:]
    for word in list(re.finditer(digit, subStr))[::-1]:
        newStr = replaceToSpace(string, word)
        if newStr:
            string = newStr
        if word.start() == 0:
            return string


def replaceToSpace(string, word):
    wordLen = word.end() - word.start()
    space = re.search(r'[.]{' + str(wordLen) + r',}', string[0:word.start()])
    if space:
        newStr = replaceAtIndex(string, space.start(), word.group(0))
        newStr = replaceAtIndex(newStr, word.start(), '.' * wordLen)
        return newStr



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

    data = read("day9.txt")
    data = uncompress(data)
    data = moveWhole(data)
    print(checksum2([int(i) if i != '.' else 0 for i in data]))
