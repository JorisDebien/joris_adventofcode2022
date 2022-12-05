count = 0

with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_4\2022_4_input.txt") as file:
    for line in file:
        # determine ranges
        first_elf, second_elf = line.split(",")            
        first_elf_start, first_elf_end = first_elf.split("-")
        second_elf_start, second_elf_end = second_elf.split("-")

        first_elf_range = range(int(first_elf_start), int(first_elf_end) + 1)
        second_elf_range = range(int(second_elf_start), int(second_elf_end) + 1)

        # check if one contains the other, and count if they do
        if any(i in first_elf_range for i in second_elf_range):
            count += 1
            
print(count)