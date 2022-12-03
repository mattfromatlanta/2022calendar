import copy
import string

file = open("day3input.txt", "r")
rucksacks = file.read().split("\n")

PRIORITIES = {}
position = 0
for letter in string.ascii_letters:
    position += 1
    PRIORITIES[letter] = position

priority_sum = 0
for sack in rucksacks:
    sack_size = int(len(sack))
    half_sack = int(sack_size/2)
    first_section = list(sack[0:half_sack])
    second_section = list(sack[half_sack:sack_size])
    for item in first_section:
        if item in second_section:
            priority_sum += PRIORITIES[item]
            break

trio_priority_sum = 0
sack_groups = []
count = 1
this_group = []
for sack in rucksacks:
    this_group.append(sack)
    if count % 3 == 0:
        sack_groups.append(copy.copy(this_group))
        this_group = []
    count += 1
for sack_group in sack_groups:
    for item in list(sack_group[0]):
        if item in list(sack_group[1]) and item in list(sack_group[2]):
            trio_priority_sum += PRIORITIES[item]
            break

print(f'priority sum {priority_sum}')
print(f'trio priority sum {trio_priority_sum}')
print('end')
