import concurrent.futures
import os
import pickle
import gzip
import tempfile
from datetime import datetime
from collections import Counter


def counterBlink(data):
    ret = Counter()
    for el, cnt in data.items():
        if el == 0:
            val = 1
            ret[val] = ret[val] + cnt if val in ret else cnt
        else:
            si = str(el)
            d, m = divmod(len(si), 2)
            if m == 0:
                val = int(si[:d])
                ret[val] = ret[val] + cnt if val in ret else cnt
                val = int(si[d:])
                ret[val] = ret[val] + cnt if val in ret else cnt
            else:
                val = el * 2024
                ret[val] = ret[val] + cnt if val in ret else cnt
    return ret

def blink(data):
    ret = []
    for el in data:
        if el == 0:
            ret.append(1)
        else:
            si = str(el)
            d, m = divmod(len(si), 2)
            if m == 0:
                ret.append(int(si[:d]))
                ret.append(int(si[d:]))
            else:
                ret.append(el * 2024)
    return ret

class ChunkIterator:
    def __init__(self, data, chunk_size):
        self.data = data
        self.chunk_size = chunk_size
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx > len(self.data):
            raise StopIteration
        self.idx += self.chunk_size
        return self.data[self.idx - self.chunk_size : self.idx]

def fileBlink(fName):
    newNames = []
    data = restore(fName)
    for ch in ChunkIterator(blink(data), 10000000):
        newNames.append(store(ch))
    return newNames


def multiBlink(fNames):
    with concurrent.futures.ProcessPoolExecutor(max_workers=12) as executor:
        ret = list(executor.map(fileBlink, fNames))
        return [item for sublist in ret for item in sublist]

def store(data):
    fName = tempfile.NamedTemporaryFile('wb').name  # dir='/mnt/data/upload/tmp'
    with gzip.open(fName, 'wb') as file:
        pickle.dump(data, file)
    return fName

def restore(fName):
    with gzip.open(fName, 'rb') as file:
        data = pickle.load(file)
    os.remove(fName)
    return data

def justRestore(fName):
    with gzip.open(fName, 'rb') as file:
        data = pickle.load(file)
    return data

def cToList(data):
    kes = list(data.keys())
    kes.sort()
    return [(k, data[k]) for k in kes]


if __name__ == '__main__':
    data = Counter([125, 17])
    for i in range(25):
        data = counterBlink(data)
        print(i, len(data), sum(data.values()), cToList(data))

    data = [125, 17]
    for i in range(25):
        data = blink(data)
        print(i, len(data), cToList(Counter(data)))

    data = [125, 17]
    fNames = [store(data)]
    for i in range(25):
        print(i, len(fNames))
        fNames = multiBlink(fNames)
    l = 0
    for fName in fNames:
        data = restore(fName)
        l += len(data)
    print(l)

    data = Counter([28, 4, 3179, 96938, 0, 6617406, 490, 816207])
    for i in range(75):
        data = counterBlink(data)
        print(i, len(data), sum(data.values()))

    data = [28, 4, 3179, 96938, 0, 6617406, 490, 816207]
    fNames = [store(data)]
    for i in range(0):
        t = datetime.now()
        newFNames = multiBlink(fNames)
        for f in fNames:
            if os.path.exists(f):
                print(f)
                os.remove(f)
        fNames = newFNames
        l = 0
        allData = []
        for fName in fNames:
            data = justRestore(fName)
            allData += data
            l += len(data)
        allData.sort()
        print(allData[:100], allData[-100:])
        print(i, l, len(fNames), datetime.now() - t)
    l = 0
    for fName in fNames:
        data = restore(fName)
        l += len(data)
    print(l)
