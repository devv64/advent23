# Dev Patel

# Part One
def part_one(file):
    map = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    f = open(file, 'r')
    lines = f.readlines()

    ans = 0
    bool = True
    for line in range(len(lines)):
        li = lines[line].split(":")
        l = li[1].split(";")
        for c in l:
            cur = c.split(',')
            for p in cur:
                p = p.strip()
                p = p.split(' ')
                if map[p[1]] < int(p[0]):
                    bool = False
        if bool:
            ans += line+1
        bool = True
    return ans

# Part Two
def part_two(file):
    map = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    f = open(file, 'r')
    lines = f.readlines()

    ans = 0
    for line in range(len(lines)):
        cur_map = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        li = lines[line].split(":")
        l = li[1].split(";")
        for c in l:
            cur = c.split(',')
            for p in cur:
                p = p.strip()
                p = p.split(' ')
                if cur_map[p[1]] < int(p[0]):
                    cur_map[p[1]] = int(p[0])
        ans += cur_map['red'] * cur_map['green'] * cur_map['blue']
    return ans

print(part_one("day2.txt"))
print(part_two("day2.txt"))
