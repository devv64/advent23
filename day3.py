# Dev Patel

file = 'day3.txt'
# file = 'tst.txt'
f = open(file, 'r')
lines = f.readlines()

def part_one(lines):
    def get_number(line, idx):
        indexes = []
        cur = 0
        for c in range(len(line)):
            if not line[c].isdigit():
                cur += 1 
                indexes.append(-1)
            else:
                indexes.append(cur)
        curIdx = indexes[idx]
        if curIdx == -1:
            return 0, idx + 1
        num = ''
        maxn = 0
        for n in range(len(indexes)):
            if indexes[n] == curIdx:
                maxn = max(maxn, n)
                num += line[n]
        return num, maxn + 1

    non = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
    acc = 0
    for l in range(1,len(lines)-1):
        symbols = [0] * len(lines[0])
        for c in range(len(lines[l])-1):
            if lines[l][c] not in non:
                symbols[c] = 1
        for j in range(l-1, l+2):
            iter = 0
            while iter < len(lines[j]) - 1:
                if symbols[max(iter-1,0)] or symbols[iter] or symbols[min(iter+1,len(symbols)-1)]:
                    num, iter = get_number(lines[j], iter)
                    acc += int(num)
                else:
                    iter += 1 
    return acc


print(part_one(lines))

def part_two(lines):
    def get_number(line, idx):
        indexes = []
        cur = 0
        for c in range(len(line)):
            if not line[c].isdigit():
                cur += 1 
                indexes.append(-1)
            else:
                indexes.append(cur)
        curIdx = indexes[idx]
        if curIdx == -1:
            return 0, idx + 1
        num = ''
        maxn = 0
        for n in range(len(indexes)):
            if indexes[n] == curIdx:
                maxn = max(maxn, n)
                num += line[n]
        return num, maxn + 1

    acc = 0
    for l in range(1,len(lines)-1):
        for c in range(len(lines[l])):
            if lines[l][c] == '*':
                gear = []
                for j in (l-1, l, l+1):
                    ci = c-1
                    while ci < c + 2:
                        num, ci = get_number(lines[j], ci)
                        if num != 0:
                            gear.append(int(num))
                if len(gear) == 2:
                    acc += gear[0] * gear[1]
    return acc

print(part_two(lines))
