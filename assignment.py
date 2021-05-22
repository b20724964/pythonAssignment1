map_1d, map_2d, mov = [], [], []
score, y, x = 0, 0, 0  # y is rabbit line coordinate, x is rabbit column coordinate
map_row = list(input("Please enter feeding map as a list: \n"))
map_count = map_row.count("[")  # to detect lines


def feeding_map_design():    # to create the two dimensional feeding map  and locate the rabbits position
    for i in range(len(map_row)):
        if map_row[i] == "*" or map_row[i] == "C" or map_row[i] == "A" or \
                map_row[i] == "P" or map_row[i] == "M" or map_row[i] == "W" or map_row[i] == "X":
            map_1d.append(map_row[i])
    for i in range(0, len(map_1d), len(map_1d) // (map_count - 1)):
        map_2d_line = []
        for j in range(len(map_1d) // (map_count - 1)):
            map_2d_line.append(j)
            map_2d_line[j] = map_1d[j + i]
        map_2d.append(map_2d_line)
    for i in range(len(map_2d)):
        for j in range(len(map_2d[0])):
            if map_2d[i][j] == "*":
                global x, y
                y = i
                x = j


feeding_map_design()

while True:    # check if the map meets the required standards before print the chart
    if len(map_2d) in range(1, 11) and len(map_2d[0]) in range(1, 11) and map_row.count("*") == 1:
        break
    else:
        print("Your feeding map have to contains one '*' for rabbit \n"   
              "The number of rows and columns will be between 1 and 10.")
        map_row = list(input("Please enter feeding map as a list again: \n"))
        map_count = map_row.count("[")
        map_1d, map_2d = [], []
        feeding_map_design()

mov_row = list(input("Please enter direction of movements as a list: \n"))
for i in range(len(mov_row)):  # to create movement order for a list
    if mov_row[i] == "U" or mov_row[i] == "D" or mov_row[i] == "L" or mov_row[i] == "R":
        mov.append(mov_row[i])

while True:     # check if the movement meets the required standards before executing
    if len(mov) in range(1, 16):
        break
    else:
        print("Direction of movement list contains between 1 and 15 movement commands")
        mov_row = list(input("Please enter direction of movements as a list again: \n"))
        mov = []

print("Your board is:")


def board():  # to print the feeding map on the screen
    for i in range(len(map_2d)):
        for j in range(len(map_2d[0])):
            print(f" {map_2d[i][j]}", end=" ")
        print()


board()


def eating():  # rabbit eating score
    global score
    if map_2d[y][x] == "C":
        score += 10
    elif map_2d[y][x] == "A":
        score += 5
    elif map_2d[y][x] == "M":
        score -= 5


for i in range(len(mov)):  # rabbit movement possibilities and consequences
    if mov[i] == "U":
        y -= 1
        if map_2d[y][x] == "W" or y == -1:  # i can write this line like 89-91 but not need
            y += 1                          # for example: list[-1][0] is not undefined
        else:                               # so i didn't change this line
            if map_2d[y][x] != "P":
                eating()
                map_2d[y][x] = "*"
                map_2d[y + 1][x] = "X"
            else:
                map_2d[y][x] = "*"
                map_2d[y + 1][x] = "X"
                break
    elif mov[i] == "D":
        y += 1
        if y == len(map_2d):
            y -= 1
        elif map_2d[y][x] == "W":
            y -= 1
        else:
            if map_2d[y][x] != "P":
                eating()
                map_2d[y][x] = "*"
                map_2d[y - 1][x] = "X"
            else:
                map_2d[y][x] = "*"
                map_2d[y - 1][x] = "X"
                break
    elif mov[i] == "L":
        x -= 1
        if map_2d[y][x] == "W" or x == -1:
            x += 1
        else:
            if map_2d[y][x] != "P":
                eating()
                map_2d[y][x] = "*"
                map_2d[y][x + 1] = "X"
            else:
                map_2d[y][x] = "*"
                map_2d[y][x + 1] = "X"
                break
    elif mov[i] == "R":
        x += 1
        if x == len(map_2d[0]):
            x -= 1
        elif map_2d[y][x] == "W":
            x -= 1
        else:
            if map_2d[y][x] != "P":
                eating()
                map_2d[y][x] = "*"
                map_2d[y][x - 1] = "X"
            else:
                map_2d[y][x] = "*"
                map_2d[y][x - 1] = "X"
                break

print("Your output should be like this: ")
board()
print(f"Your score is: {score}")
