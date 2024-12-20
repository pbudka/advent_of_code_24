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
        if i % 1000 == 0:
            print(string[0:200], i, word.start(), word.group(0))
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

class NumIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if not self.index:
            raise StopIteration
        val = None
        end = None
        data = self.data
        for i in range(self.index, -1, -1):
            if not data[i] is None:
                if val is None:
                    val = data[i]
                    end = i
                elif val != data[i]:
                    self.index = i
                    return val, i+1, end
            elif not val is None:
                self.index = i
                return val, i+1, end
        else:
            if not val is None:
                self.index = 0
                return val, 0, end


class NoNeIterator:
    def __init__(self, data, size):
        self.data = data
        self.size = size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        data = self.data
        while True:
            try:
                self.index = index = data.index(None, self.index)
            except ValueError:
                raise StopIteration
            if index + self.size > len(data):
                self.index = len(data)
                raise StopIteration
            for i in range(index, index + self.size):
                if data[i]:
                    self.index = i
                    break
            else:
                self.index = index + self.size
                break
        return index


def moveWhole(data):
    i = 0
    for num, s, e in NumIterator(data[:]):
        ln = e - s + 1
        i += 1
        if i % 1000 == 0:
            print(num, s, e, data[:100], data[-100:])
        for space in NoNeIterator(data, ln):
            if space < s:
                for i in range(space, space + ln):
                    data[i] = num
                for i in range(s, e + 1):
                    data[i] = None
            break
    return data


def checksum(data):
    s = 0
    for i in range(0, len(data)):
        if data[i]:
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
    print(checksum(data))

    data = uncompress("233313312141413140225")
    print(data)
    data = moveWhole(data)
    print(data)
    print(checksum(data))

    data = read("day9.txt")
    data = uncompress(data)
    print(data[:100], data[-100:])
    data = moveWhole(data)
    print(data[:100], data[-100:])
    print(checksum(data))
    print(90546720886)
