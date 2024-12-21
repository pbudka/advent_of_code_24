import concurrent.futures
import os
import pickle
import tempfile

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
    for ch in ChunkIterator(blink(data), 1000000):
        newNames.append(store(ch))
    return newNames


def multiBlink(fNames):
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        ret = list(executor.map(fileBlink, fNames))
        return [item for sublist in ret for item in sublist]

def store(data):
    fName = tempfile.NamedTemporaryFile('wb').name
    with open(fName, 'wb') as file:
        pickle.dump(data, file)
    return fName

def restore(fName):
    with open(fName, 'rb') as file:
        data = pickle.load(file)
    os.remove(fName)
    return data

if __name__ == '__main__':

    data = [125, 17]
    for i in range(25):
        data = blink(data)
        print(i, len(data))

    # data = [125, 17]
    # for i in range(25):
    #     data = multiBlink(data)
    #     print(i, len(data))

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

    data = [28, 4, 3179, 96938, 0, 6617406, 490, 816207]
    fNames = [store(data)]
    for i in range(55):
        print(i, len(fNames))
        fNames = multiBlink(fNames)
    l = 0
    for fName in fNames:
        data = restore(fName)
        l += len(data)
    print(l)
