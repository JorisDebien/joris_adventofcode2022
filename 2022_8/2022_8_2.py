array = []
current_scenic_score = 0

with open(r"/Users/jdebien/src/joris_adventofcode2022/2022_8/2022_8_input.txt") as file:
    for line in file:
        row = [*line.strip()]
        array.append(row)


def calculate_scenic_score(list_of_trees, tree_height):
    if len(list_of_trees) == 0:
        return 0

    for x in range(0, len(list_of_trees)):
        if list_of_trees[x] >= tree_height:
            return x + 1
    
    return len(list_of_trees)


for row in array:
    for i in range(0, len(row)):
        tree_height = int(row[i])
        left_row = [int(x) for x in row[:i]]
        left_row.reverse()
        right_row = [int(x) for x in row[i+1:]]
        up_column = [int(row[i]) for row in array[:array.index(row)]]
        up_column.reverse()
        down_column = [int(row[i]) for row in array[array.index(row)+1:]]

        left_score = calculate_scenic_score(left_row, tree_height)
        right_score = calculate_scenic_score(right_row, tree_height)
        up_score = calculate_scenic_score(up_column, tree_height)
        down_score = calculate_scenic_score(down_column, tree_height)

        scenic_score = left_score * right_score * up_score * down_score

        if scenic_score > current_scenic_score:
            print(scenic_score)
            current_scenic_score = scenic_score
            

print("Answer: " + str(current_scenic_score))


