# Advent of Code - 2020 - Day 3

filerows = open('d3_input.txt')
# Map description:       . = open space      # = tree
map = []
for row in filerows:
    map.append(row.strip())


def tree_counter(map, right, down):
    map_width = len(map[0])
    path = 0
    pos = [0, 0]    # x (width), y (depth)
    num_of_trees = 0
    for r in map:
        # print(' position: ' + str(pos))
        # if map ends, loop it again
        if pos[0] >= map_width:
            pos[0] = pos[0] - map_width
        if pos[1] == path:
            # look for trees!
            if (r[pos[0]] == '#') & (pos[1] == path):
                num_of_trees += 1
            # move
            pos = [pos[0] + right, pos[1] + down]
        path += 1
    return num_of_trees


# Part One

part_one = tree_counter(map, 3, 1)
print(' - Part One - Number of trees found: ' + str(part_one))

# Part Two

s_one = tree_counter(map, 1, 1)
# print('   -- Trees in slope 1: ' + str(s_one))
s_two = part_one
# print('   -- Trees in slope 2: ' + str(s_two))
s_three = tree_counter(map, 5, 1)
# print('   -- Trees in slope 3: ' + str(s_three))
s_four = tree_counter(map, 7, 1)
# print('   -- Trees in slope 4: ' + str(s_four))
s_five = tree_counter(map, 1, 2)
# print('   -- Trees in slope 5: ' + str(s_five))
print(' - Part Two - Number of trees multiplied: ' + str(s_one * s_two * s_three * s_four * s_five))

