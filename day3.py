import re

pattern = re.compile(r'(do\(\)|don\'t\(\)|mul\((\d+),(\d+)\))')
enabled = True

def sumMultiples(input):
    global enabled
    total = 0
    for nums in re.findall(pattern, input):
        what = nums[0][:3]
        if what == 'don':
            enabled = False
        elif what == 'do(':
            enabled = True
        elif enabled:
            total += int(nums[1]) * int(nums[2])
    return total


def sumAllMultiples(fname):
    total = 0
    with open(fname, "r") as f:
        for line in f.readlines():
            total += sumMultiples(line)
            print(len(line), total)
    return total


if __name__ == '__main__':
    ti = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    print(re.findall(pattern, ti))
    print(sumMultiples(ti))
    print(sumAllMultiples("day3.txt"))

