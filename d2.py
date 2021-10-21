# Advent of Code - 2020 - Day 2

# Part one

filerows = open('d2_input.txt')
num_valid_passwords = 0
for row in filerows:
    least = int(row.split('-')[0])
    most = int(row.split('-')[1].split(' ')[0])
    letter = row.split(' ')[1][0]
    password = row.split(' ')[2].strip()
    # print('The letter: ' + str(letter) + ' must occur at least ' + str(least) + ' times and at most ' + str(most) + ' times in the password: ' + str(password))
    letter_counter = 0
    for l in password:
        if l == letter:
            letter_counter += 1
    if (letter_counter >= least) & (letter_counter <= most):
        num_valid_passwords += 1

print(' - Part One: The number of valid passwords is: ' + str(num_valid_passwords))

# Part two

filerows = open('d2_input.txt')
num_valid_passwords = 0
for row in filerows:
    pos_one = int(row.split('-')[0])
    pos_two = int(row.split('-')[1].split(' ')[0])
    letter = row.split(' ')[1][0]
    password = row.split(' ')[2].strip()
    # print('The letter: ' + str(letter) + ' must occur at position ' + str(pos_one) + ' or ' + str(pos_two) + ' but not in both in the password: ' + str(password))
    if (password[pos_one-1] == letter or password[pos_two-1] == letter) and password[pos_one-1] != password[pos_two-1]:
        num_valid_passwords += 1

print(' - Part Two: The number of valid passwords is: ' + str(num_valid_passwords))
