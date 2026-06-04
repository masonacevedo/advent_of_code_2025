f_name = "4_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

rawGrid = [line.replace("\n","") for line in lines]
grid = [list(char for char in line) for line in rawGrid]

def getNeighbors(row, col):
    
    neighbors = []

    topNeighbor = (row-1, col)
    botNeighbor = (row+1, col)
    leftNeighbor = (row, col-1)
    rightNeihghbor = (row, col+1)

    topLeftNeighbor = (row-1, col-1)
    topRightNeighbor = (row-1, col+1)
    botLeftNeighbor = (row+1, col-1)
    botRightNeighbor = (row+1, col+1)

    if row == 0 and col == 0:
        neighbors = [rightNeihghbor, botRightNeighbor, botNeighbor]
    elif row == 0 and col == len(grid[0])-1:
        neighbors = [leftNeighbor, botLeftNeighbor, botNeighbor]
    elif row == len(grid)-1 and col == 0:
        neighbors = [topNeighbor, topRightNeighbor, rightNeihghbor]
    elif row == len(grid)-1 and col == len(grid[0])-1:
        neighbors = [leftNeighbor, topLeftNeighbor, topNeighbor]
    
    elif row == 0:
        neighbors = [leftNeighbor, botLeftNeighbor, botNeighbor, botRightNeighbor, rightNeihghbor]
    elif col == 0:
        neighbors = [topNeighbor, topRightNeighbor, rightNeihghbor, botRightNeighbor, botNeighbor]
    elif row == len(grid)-1:
        neighbors = [leftNeighbor, topLeftNeighbor, topNeighbor, topRightNeighbor, rightNeihghbor]
    elif col == len(grid[0])-1:
        neighbors = [botNeighbor, botLeftNeighbor, leftNeighbor, topLeftNeighbor, topNeighbor]
    else:
        neighbors = [topNeighbor, topRightNeighbor, rightNeihghbor, botRightNeighbor, botNeighbor, botLeftNeighbor, leftNeighbor, topLeftNeighbor]

    return neighbors

def isRoll(coords):
    # print("coords:", coords)
    return grid[coords[0]][coords[1]] == "@"


def getRemovable():
    removable = []
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            
            if grid[row][col] != "@":
                continue
            # print("len(grid):", len(grid))
            # print("len(grid[0]):", len(grid[0]))

            # print("row:", row)
            # print("col:", col)
            neighbors = getNeighbors(row, col)
            # print("neighbors:", neighbors)
            # input("enter to con")
            # print("neighbors:", neighbors)
            rolls = [isRoll(n) for n in neighbors]
            rollCount = sum(rolls)
            if rollCount < 4:
                # print("accessilbe!")
                removable.append((row, col))
            # else:
                # print("not accessible")
            
            # input("enter to con")
    return removable

ans = 0
while len(getRemovable()) > 0:
    coords = getRemovable()
    ans += len(coords)
    for coord in coords:
        row, col = coord
        grid[row][col] = "."
    

print("ans:", ans)