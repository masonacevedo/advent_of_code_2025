import math

f_name = "7_example.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

grid = [line.replace("\n","") for line in lines]
grid = [[char for char in line] for line in grid]

def printGrid(grid):
    for row in grid:
        print("".join([str(e) for e in row]))

printGrid(grid)

def propogate(G, splitCount):
    for row in range(0, len(G)):
        for col in range(0, len(G[0])):
            if G[row][col] != "|":
                continue
            if row == len(G)-1:
                continue
            
            neighborBelow = G[row+1][col]
            if neighborBelow == ".":
                G[row+1][col] = "|"
            elif neighborBelow == "^":
                G[row+1][col-1] = "|"
                G[row+1][col+1] = "|"
                splitCount += 1
    return splitCount

splitCount = propogate(grid, 0)
print("\n")
printGrid(grid)

nums = [1,2,3,4,5,6,7,8,9]

firstRow = 0
firstCol = grid[0].index("|")
grid[firstRow][firstCol] = 1
print("\n")
printGrid(grid)

def count():
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] not in nums:
                continue
            if row == len(grid)-1:
                continue
            currentNum = grid[row][col]
            if grid[row+1][col] == "^":
                existingLeft = grid[row+1][col-1]
                existingRight = grid[row+1][col+1]
                if existingLeft == "|":
                    grid[row+1][col-1] = currentNum
                else:
                    grid[row+1][col-1] = grid[row+1][col-1] + currentNum

                if existingRight == "|":
                    grid[row+1][col+1] = currentNum
                else:
                    grid[row+1][col+1] = grid[row+1][col+1] + currentNum
            else:
                grid[row+1][col] = grid[row][col]
            
            printGrid(grid)
            input("enter to con")

# import copy
# print("\n")
# lastGrid = copy.deepcopy(grid)
# count()
# while grid != lastGrid:
#     count()
#     printGrid(grid)
#     input("enter to con")
    
printGrid(grid)
count()
printGrid(grid)
# ans = countPaths(grid, 0, grid[0].index("|"))
# print("ans:", ans)

lastRow = grid[-1]
print("lastRow:", lastRow)
lastNums = list(filter(lambda e: type(e) == int, lastRow))
print("lastNums:", lastNums)
print(sum(lastNums))