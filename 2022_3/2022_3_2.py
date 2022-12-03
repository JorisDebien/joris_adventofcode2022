priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority_sum = 0
group_size = 3
groups = []
common_letters = []
listedFile = []

with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_3\2022_3_input.txt") as file:
    for line in file:
        listedFile.append(line)

# break into groups
for i in range(0, len(listedFile), group_size):
    groups.append(listedFile[i:i+group_size])

# check priority sum of each group
for group in groups:

    common_letter = list(set(group[0]) & set(group[1]) & set(group[2]))
    if "\n" in common_letter:
        common_letter.remove("\n")
    common_letters.append(common_letter[0])


for letter in common_letters:
    priority_sum += priority.index(letter) + 1

print(priority_sum)