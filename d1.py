# Advent of Code - 2020 - Day 1

filerows = open('d1_input.txt')
numbers = []

for row in filerows:
    numbers.append(row.strip())

# Part One

solved = False
for x in numbers:
    if solved is True:
        break
    for y in numbers:
        if int(x) + int(y) == 2020:
            print(' - Part one: the product of the numbers ' + str(x) + ' and ' + str(y) + ' is: ' + str(int(x) * int(y)))
            solved = True
            break

# Part Two

solved = False
for x in numbers:
    if solved is True:
        break
    for y in numbers:
        if solved is True:
            break
        for z in numbers:
            if int(x) + int(y) + int(z) == 2020:
                print(' - Part two: the product of the numbers ' + str(x) + ' and ' + str(y) + ' and ' + str(z) + ' is: ' + str(int(x) * int(y) * int(z)))
                solved = True
                break

