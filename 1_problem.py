f_name = "1_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

position = 50
count = 0


def processLine(line, position, count):
    movement = int(line[1:-1])

    i = movement
    for _ in range(0, movement):
        if "L" in line:
            position -= 1
        else:
            position += 1

        if position % 100 == 0:
            count += 1
    return position, count


for line in lines:
    position, count = processLine(line, position, count)

print("count:", count)