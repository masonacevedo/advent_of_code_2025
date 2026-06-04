import math

f_name = "7_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

grid = [line.replace("\n","") for line in lines]
grid = [[char for char in line] for line in grid]

def printGrid(grid):
    for row in grid:
        print("".join(row))

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
printGrid(grid)
print("splitCount:", splitCount)