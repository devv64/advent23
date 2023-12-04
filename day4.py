# Dev Patel

file = 'day4.txt'
# file = 'tst.txt'
f = open(file, 'r')
lines = f.readlines()

def part_one(lines):
    acc = 0
    for line in lines:
        card = line.split(':')
        lists = card[1].split('|')
        wins = lists[0].strip().split(' ')
        mine = lists[1].strip().split(' ')
        ws = -1
        for num in mine:
            if num in wins and num != '':
                ws += 1
        if ws != -1:
            cur = 1
            for _ in range(ws):
                cur *= 2
            acc += cur
    return acc

print(part_one(lines))

def part_two(lines):
    amts = [1] * len(lines)
    for l in range(len(lines)):
        card = lines[l].split(':')
        lists = card[1].split('|')
        wins = lists[0].strip().split(' ')
        mine = lists[1].strip().split(' ')
        ws = 1
        for num in mine:
            if num in wins and num != '':
                ws += 1
        for i in range(l+1, l+ws):
            amts[i] += 1 * amts[l]
    return sum(amts)

print(part_two(lines))
