array = []
visible_trees = 0

with open(r"/Users/jdebien/src/joris_adventofcode2022/2022_8/2022_8_input.txt") as file:
    for line in file:
        row = [*line.strip()]
        array.append(row)


for row in array:
    for i in range(0, len(row)):
        is_visible = False
        left_row = [int(x) for x in row[:i]]
        right_row = [int(x) for x in row[i+1:]]
        up_column = [int(row[i]) for row in array[:array.index(row)]]
        down_column = [int(row[i]) for row in array[array.index(row)+1:]]

        if len(left_row) == 0 or max(left_row) < int(row[i]):
            is_visible = True
        elif len(right_row) == 0 or max(right_row) < int(row[i]):
            is_visible = True
        elif len(up_column) == 0 or max(up_column) < int(row[i]):
            is_visible = True
        elif len(down_column) == 0 or max(down_column) < int(row[i]):
            is_visible = True
        
        if is_visible:
            visible_trees += 1


print(visible_trees)