current_stack = [["Z", "P", "B", "Q", "M", "D", "N"], 
                ["V", "H", "D", "M", "Q", "Z", "L", "C"], 
                ["G", "Z", "F", "V", "D","R", "H", "Q"],
                ["N", "F", "D", "G", "H"],
                ["Q", "F", "N"],
                ["T", "B", "F", "Z", "V", "Q", "D"],
                ["H", "S", "V", "D", "Z", "T", "M", "Q"],
                ["Q", "N", "P", "F", "G", "M"],
                ["M", "R", "W", "B"]]


def move_crane(crane_from, crane_to):
    stack_from = crane_from - 1
    stack_to = crane_to - 1

    box = current_stack[stack_from].pop(0)
    current_stack[stack_to].insert(0, box)

    print(current_stack)


with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_5\2022_5_input.txt") as file:
    for line in file:
        crane_quantity = int(line.split()[1])
        crane_from = int(line.split()[3])
        crane_to = int(line.split()[5])
        
        for x in range(0, crane_quantity):
            move_crane(crane_from, crane_to)

for stack in current_stack:
    print(stack[0])