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
    print(string)
    blank = re.compile(r'[.]+')
    digit = re.compile(r'(0+|1+|2+|3+|4+|5+|6+|7+|8+|9+)')
    subStr = string[:]
    end = 0
    while True:
        finds = list(re.finditer(digit, subStr))
        if not finds:
            return string
        word = finds[-1]
        wordLen = word.end() - word.start()
        pEnd = end
        newStr, end = replaceToSpace(blank, string, word, wordLen, pEnd)
        if newStr is None:
            if word.start() == 0:
                return string
            subStr = subStr[0:word.start()]
        else:
            if end > word.start() + pEnd:
                return newStr
            string = newStr
            subStr = string[end:word.start()+pEnd]


def replaceToSpace(blank, string, word, wordLen, end):
    for space in blank.finditer(string):
        if wordLen <= space.end() - space.start() and space.start() < word.start() + end:
            newStr = replaceAtIndex(string, space.start(), word.group(0))
            newStr = replaceAtIndex(newStr, word.start() + end, '.' * wordLen)
            return newStr, space.start() + wordLen
    return None, end


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

    data = uncompress("2333133121414131402")
    print( moveWhole(data) )

#     data = read("day9.txt")
#     data = uncompress(data)
#     print(data)
#     move(data)
#     print(data)
#     print(checksum(data))
