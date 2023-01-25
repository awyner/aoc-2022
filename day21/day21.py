import operator
from z3 import *

ops = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv,
       '==':operator.eq}


def main():
    monkes = {}
    with open("day21\\input2.txt") as f:
        for line in f:
            line = line.strip().split()
            line[0] = line[0][:-1]
            if line[1].isdigit():
                monkes[line[0]] = int(line[1])
            else:
                monkes[line[0]] = [line[1], line[3], line[2]]
        monkes['root'][2] = '=='
        print(monkes)
    current = 'root'
    root = False
    count = 356_000_000_000_0
    # while not root:
    monkes['humn'] = 0
    root = search(monkes, current)
    count +=1
    print(root)
    

def search(dict, current):
    if not isinstance(dict[current], int):
        left = dict[current][0]
        right = dict[current][1]
        print(current, left, right, dict[current][2])
        left = search(dict, left)
        right = search(dict, right)
        if current == 'root':
            print(left, right)
        op = dict[current][2]
        return ops[op](left, right)
    else:
        return dict[current]


main()
