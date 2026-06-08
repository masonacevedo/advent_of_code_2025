
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

shapes = splitShapeLines(shapeLines)

shapeMap = {int(shape[0][0:-1]): buildShape(shape) for shape in shapes}
print(shapeMap)
print(sizes)

def extractRequirements(size):
    dims, counts = size.split(":")
    rowString, colString = dims.split("x")
    rows = int(rowString)
    cols = int(colString)
    countsRequired = counts.split(" ")[1:]
    return rows, cols, [int(count) for count in countsRequired]

print(extractRequirements(sizes[1]))

def placeInGrid(grid, shape, startRow, startCol):
    
    shapeHeight = len(shape)
    shapeWidth = len(shape[0])

    if (startRow + shapeHeight) > len(grid):
        # print("rows too big!")
        return None
    
    if (startCol + shapeWidth) > len(grid[0]):
        # print('cols too big!')
        return None
    
    ans = copy.copy(grid)
    for row in range(0, shapeHeight):
        for col in range(0, shapeWidth):
            shapeChar = shape[row][col]
            gridChar = grid[row + startRow][col + startCol]
            if gridChar == "#" and shapeChar == "#":
                # print("row:", row)
                # print("col:", col)
                # print("shapeChar:", shapeChar)
                # print("gridChar:", gridChar)
                # print("overlapping!")
                return None
            
            if gridChar == "#" or shapeChar == "#":
                ans[row+startRow][col+startCol] = "#"
            else:
                ans[row+startRow][col+startCol] = "."
    return ans


grid = [
    [".",".","."],
    [".",".","."],
    [".",".","."]
]

print(shapeMap)
first = placeInGrid(grid, shapeMap[0], 0,0)
print("first placement :", first)

# second = placeInGrid(first, shapeMap[1], 1, 0)
# print("second placement:", second)