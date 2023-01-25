def main():
    items = []
    itemsCopy = []
    with open("day20\\input.txt") as f:
        id = 0
        for line in f:
            items.append([int(line.strip()) * 811589153, id])
            itemsCopy.append([int(line.strip()) * 811589153, id])
            id += 1
    for x in range(10):
        items = searchList(items, itemsCopy)
        print("Round", x, "complete")
        
    # print(items)
    for x in range(len(items)):
        if items[x][0] == 0:
            index = x
    res1 = (1000 + index) % len(items)
    res2 = (2000 + index) % len(items)
    res3 = (3000 + index) % len(items)
    print(items[res1][0], items[res2][0], items[res3][0])
    print(items[res1][0] + items[res2][0] + items[res3][0])


def searchList(lst, lstCopy):
    index = 0
    for copy in lstCopy:
        for item in lst:
            if copy[1] == item[1]:
                current = item
                break
            index += 1
        del lst[index]
        if current[0] > 0:
            target = (current[0] + index) % (len(lst))
        elif current[0] <= 0:
            target = (current[0] + index) % (len(lst))
        if target == 0:
            target = len(lst)
        lst.insert(target, current)
        index = 0
    return lst


main()
