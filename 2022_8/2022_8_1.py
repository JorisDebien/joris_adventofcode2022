array = []
visible_trees = 0

with open(r"/Users/jdebien/src/joris_adventofcode2022/2022_8/2022_8_input.txt") as file:
    for line in file:
        row = [*line.strip()]
        array.append(row)


# multiple trees of the same height --> index is going crazy because it returns the first item of that height!

for row in array:
    print("row" + str(array.index(row)))
    for tree in row:
        print("Tree" + str(row.index(tree)))
        is_visible = False
        left_row = row[:row.index(tree)]
        right_row = row[row.index(tree)+1:]
        up_column = 0
        down_column =0

        if len(left_row) == 0:
            is_visible = True
        elif max([int(x) for x in left_row]) < int(tree):
            is_visible = True
        elif len(right_row) == 0:
            is_visible = True
        elif max([int(x) for x in right_row]) < int(tree):
            is_visible = True
        
        if is_visible:
            visible_trees += 1


print(visible_trees)