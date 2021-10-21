# Advent of Code - 2020 - Day 4

# Merge rows as a single line of information per passport and store them in passports[]
file_rows = open('d4_input.txt')
passports = []
temp = ''
for row in file_rows:
    if row.strip() == '':
        if temp != '':
            passports.append(temp)
        temp = ''
    else:
        if temp == '':
            temp = row.strip()
        else:
            temp += ' ' + row.strip()
if temp != '':
    passports.append(temp)

# Split up the details in the passports and make a full list of passport details
full_passports = []
for p in passports:
    details = {}
    p_details = p.split(' ')
    for d in p_details:
        k = d.split(':')[0]
        v = d.split(':')[1]
        details[k] = v
    full_passports.append(details)

#   byr (Birth Year)
#   iyr (Issue Year)
#   eyr (Expiration Year)
#   hgt (Height)
#   hcl (Hair Color)
#   ecl (Eye Color)
#   pid (Passport ID)
#   cid (Country ID)


# - Part one -

# Count the number of valid passports -
#   those that have all required fields. Treat cid as optional.
#   In your batch file, how many passports are valid?

num_valid = 0
for p in full_passports:
    # print(str(p) + '   << cid: ' + str(p.get('cid')) + ' type: ' + str(type(p.get('cid'))))
    if (len(p) == 8) or (len(p) == 7 and p.get('cid') is None):
        num_valid += 1


print(' - Part One - Number of valid passports: ' + str(num_valid))

# - Part two - Add more validation
#    cid (Country ID) - ignored, missing or not.

num_valid = 0
for p in full_passports:
    valid = True
    if (len(p) == 8) or (len(p) == 7 and p.get('cid') is None):
        # print(str(p) + '   << cid: ' + str(p.get('cid')) + ' type: ' + str(type(p.get('cid'))))

        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        byr = int(p.get('byr'))
        if byr < 1920 or byr > 2002:
            valid = False

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        iyr = int(p.get('iyr'))
        if iyr < 2010 or iyr > 2020:
            valid = False

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        eyr = int(p.get('eyr'))
        if eyr < 2020 or eyr > 2030:
            valid = False

        # hgt (Height) - a number followed by either cm or in:
        #     If cm, the number must be at least 150 and at most 193.
        #     If in, the number must be at least 59 and at most 76.
        hgt_raw = str(p.get('hgt'))
        if hgt_raw.find('cm') > 0:
            hgt = int(hgt_raw.split('cm')[0])
            if hgt < 150 or hgt > 193:
                valid = False
        else:
            hgt = int(hgt_raw.split('in')[0])
            if hgt < 59 or hgt > 76:
                valid = False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
        hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        hcl = str(p.get('hcl'))
        if (hcl[0] != '#') or (len(hcl) != 7):
            valid = False
        # print('hcl: ' +str(hcl) + '    hcl[1:]: ' + str(hcl[1:]))
        for h in str(hcl[1:]):
            found = False
            for c in hex:
                if h == c:
                    found = True
            if found is False:
                valid = False
                break

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        ecl = str(p.get('ecl'))
        found = False
        for e in eye:
            if ecl == e:
                found = True
        if found is False:
            valid = False

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        dec = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        pid = str(p.get('pid'))
        if len(pid) != 9:
            valid = False
        else:
            found = False
            for p in pid:
                for d in dec:
                    if p == d:
                        found = True
                if found is False:
                    valid = False
                    break

        if valid:
            num_valid += 1

print(' - Part Two - Number of valid passports: ' + str(num_valid))

