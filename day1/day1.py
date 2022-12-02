file = open('input 1a', 'r')
data = file.read().split("\n")
numbers = []
for datum in data:
    if datum != '':
        numbers.append(float(datum))
    else:
        numbers.append(-1)
max_elf = 0
second_elf = 0
third_elf = 0
current_elf = 0
for number in numbers:
    if number == -1:
        if current_elf >= max_elf:
            third_elf = second_elf
            second_elf = max_elf
            max_elf = current_elf
        elif current_elf >= second_elf:
            third_elf = second_elf
            second_elf = current_elf
        elif current_elf > third_elf:
            third_elf = current_elf
        current_elf = 0
        continue
    else:
        current_elf += number
# if max_elf < current_elf:
#     max_elf = current_elf
all_elfs = max_elf + second_elf + third_elf
print(all_elfs)
print('end')
