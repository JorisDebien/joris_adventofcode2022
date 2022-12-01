elfArray = []

with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_1\2022_1_input.txt") as file:
    tempSum = 0
    for i in file:
        if i != "\n":
            tempSum += int(i)           
        elif i == "\n":
            elfArray.append(tempSum)
            tempSum = 0

print(max(elfArray))
