elf_list = []

with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_1\2022_1_input.txt") as file:
    tempSum = 0
    for i in file:
        if i != "\n":
            tempSum += int(i)           
        elif i == "\n":
            elf_list.append(tempSum)
            tempSum = 0

# Solution for first excercise
print(max(elf_list))

# Solution for second excercise
elf_list.sort()
max_elves = elf_list[-3:]
maxSum = 0

for elf in max_elves:
    maxSum += elf

print(maxSum)
