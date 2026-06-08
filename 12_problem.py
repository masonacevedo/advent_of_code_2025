
import copy

f_name = "12_example.txt"
with open(f_name, "r+") as f:
    lines = f.readlines()


clean_lines = [line.replace("\n", "") for line in lines]


def isSize(l):
    return "x" in l

sizes = list(filter(
    isSize,
    clean_lines
))
shapeLines = list(filter(
    lambda l: not(isSize(l)),
    clean_lines
))

def splitShapeLines(lines):
    ans = []
    currentShape = []
    for line in lines:
        hasNum = [str(i) in line for i in range(0, 10)]
        if any(hasNum):
            ans.append(currentShape)
            currentShape = [line]
        else:
            currentShape.append(line)
    del ans[0]
    ans.append(currentShape)
    return ans


def buildShape(shape):
    ansIndex = shape[0]
    grid = []
    for line in shape[1:-1]:
        grid.append(line)
    return grid

shapeLines = splitShapeLines(shapeLines)

shapeMapping = {int(shape[0][0:-1]): buildShape(shape) for shape in shapeLines}
print(shapeMapping)
print(sizes)

def extractRequirements(size):
    dims, counts = size.split(":")
    rowString, colString = dims.split("x")
    rows = int(rowString)
    cols = int(colString)
    countsRequired = counts.split(" ")[1:]
    return rows, cols, [int(count) for count in countsRequired]

print(extractRequirements(sizes[1]))

def placeInGrid(grid, shape, startRow, startCol, availableSquares):
    
    shapeHeight = len(shape)
    shapeWidth = len(shape[0])

    if (startRow + shapeHeight) > len(grid):
        # print("rows too big!")
        return False
    
    if (startCol + shapeWidth) > len(grid[0]):
        # print('cols too big!')
        return False
    
    usedSpots = []
    for row in range(0, shapeHeight):
        for col in range(0, shapeWidth):
            shapeChar = shape[row][col]
            gridChar = grid[row + startRow][col + startCol]
            if gridChar == "#" and shapeChar == "#":
                return False
            elif gridChar == "#" and shapeChar == ".":
                pass
            elif gridChar == "." and shapeChar == "#":
                usedSpots.append((row + startRow, col+startCol))
            else:
                pass
    for spot in usedSpots:
        availableSquares.remove(spot)
        row, col = spot
        grid[row][col] = "#"
    
    return True

NUMROWS = 6
NUMCOLS = 3
GRID = [["." for _ in range(0, NUMCOLS)] for _ in range(0, NUMROWS)]

AVAILABLE_SQUARES = set([(row, col) for row in range(0, NUMROWS) for col in range(0, NUMCOLS)])

print(GRID)
print(len(AVAILABLE_SQUARES))
placeInGrid(GRID, shapeMapping[0], 0, 0, AVAILABLE_SQUARES)
print(GRID)
print(len(AVAILABLE_SQUARES))

# def shapeSize(shape):
#     return sum((row.count("#") for row in shape))

# def bestPlacements(shapeMap, grid, placementCounts, availableSquares):
#     ans = []
#     for shapeIndex, shape in shapeMap.items():
#         if shapeSize(shape) > len(availableSquares):
#             continue
#         # availableSquares = 
#     return ans
        


# def bestPlacementsWrapper(shapeMap, numRows, numCols):
#     grid = [["." for _ in range(numCols)] for _ in range(0, numRows)]
#     placementCounts = {shape:0 for shape in shapeMap}
#     availableSquares = set([(row, col) for row in range(0, numRows) for col in range(0, numCols)])
#     print(f'availableSquares: {availableSquares}')
#     input("enter to con")
#     return bestPlacements(shapeMap, grid, placementCounts, availableSquares)


# def findPlacements(shapes):
#     ans = {}
#     for row in range(0, 11):
#         for col in range(0, 11):
#             key = (row, col)
#             ans[key] = bestPlacementsWrapper(shapes, row, col)
#     return ans
# findPlacements(shapeMapping)