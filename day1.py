# Dev Patel

import re

# Part One
def find_calibration_value(line):
    l = re.sub("[^0-9]", "", line)
    return int(l[0] + l[-1])

def calibrate(file):
    f = open(file, 'r')
    lines = f.readlines()

    count = 0
    for line in lines:
        count += find_calibration_value(line)

    return count

print(calibrate('day1.txt'))

# Part Two
def new_calibration_value(line):
    map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for word, number in map.items():
        line = line.replace(word, word+number+word)

    l = re.sub("[^0-9]", "", line)

    return int(l[0] + l[-1])

def new_calibrate(file):
    f = open(file, 'r')
    lines = f.readlines()

    count = 0
    for line in lines:
        count += new_calibration_value(line)

    return count

print(new_calibrate('day1.txt'))
