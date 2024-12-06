def isInOrder(pages, orderRules):
    orderRules = orderRules[:]
    pages = pages[:]
    pages.reverse()
    fixed = False
    fixedOrder = []
    while pages:
        p = pages.pop()
        # print("inspect page", p)
        for page in pages:
            if (page, p) in orderRules:
                print("rule ", (page, p), " breaks order for page", p)
                pages.insert(pages.index(page),p)
                fixed = True
                break
            if (p, page) in orderRules:
                # print("rule ", (page, p), " fine for page", p)
                orderRules.remove((p, page))
        else:
            fixedOrder.append(p)
    return fixed, fixedOrder

def sumMiddlePages(allPages, orderRules):
    totalOk = 0
    totalFixed = 0
    for pages in allPages:
        fixed, fixedOrder =  isInOrder(pages, orderRules)
        middle = fixedOrder[(len(pages)-1) // 2]
        print("pages", pages, "fixed?", fixed, "fixed", fixedOrder, "fixed middle value", middle)
        if fixed:
            totalFixed += middle
        else:
            totalOk += middle
    print("totalOk", totalOk, "totalFixed", totalFixed)

def readRules(fname):
    ret = []
    with open(fname, "r") as f:
        lines = [l[:-1] for l in f.readlines()]
    for l in lines:
        spl = l.split("|")
        ret.append((int(spl[0]), int(spl[1])))
    print(len(ret))
    print(ret)
    return ret

def readPages(fname):
    ret = []
    with open(fname, "r") as f:
        lines = [l[:-1] for l in f.readlines()]
    for l in lines:
        ret.append([int(s) for s in l.split(",")])
    print(len(ret))
    print(ret)
    return ret


if __name__ == '__main__':
    orderRulesEx = [(47, 53),
                    (97, 13),
                    (97, 61),
                    (97, 47),
                    (75, 29),
                    (61, 13),
                    (75, 53),
                    (29, 13),
                    (97, 29),
                    (53, 29),
                    (61, 53),
                    (97, 53),
                    (61, 29),
                    (47, 13),
                    (75, 47),
                    (97, 75),
                    (47, 61),
                    (75, 61),
                    (47, 29),
                    (75, 13),
                    (53, 13)]
    pagesEx = [[75, 47, 61, 53, 29],
               [97, 61, 53, 29, 13],
               [75, 29, 13],
               [75, 97, 47, 61, 53],
               [61, 13, 29],
               [97, 13, 75, 29, 47]]
    sumMiddlePages(pagesEx, orderRulesEx)

    rulesMy = readRules("day5.txt")
    pagesMy = readPages("day5b.txt")
    sumMiddlePages(pagesMy, rulesMy)
