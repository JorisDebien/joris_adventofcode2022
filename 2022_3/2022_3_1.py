priority = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
priority_sum = 0

with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_3\2022_3_input.txt") as file:
    common_letters = []

    for line in file:
        first_compartiment, second_compartiment = line[:len(line)//2], line[len(line)//2:]
        common_letter = list(set(first_compartiment) & set(second_compartiment))
        common_letters.append(common_letter[0])
    
    for letter in common_letters:
        priority_sum += priority.index(letter) + 1

print(priority_sum)