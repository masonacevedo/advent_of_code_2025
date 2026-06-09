
import copy

f_name = "12_input.txt"
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
    grid = []
    for line in shape[1:-1]:
        grid.append(line)
    return tuple(tuple(char for char in line) for line in shape[1:-1])
    # return grid

shapeLines = splitShapeLines(shapeLines)

shapeMapping = {int(shape[0][0:-1]): buildShape(shape) for shape in shapeLines}

def extractRequirements(size):
    dims, counts = size.split(":")
    rowString, colString = dims.split("x")
    rows = int(rowString)
    cols = int(colString)
    countsRequired = counts.split(" ")[1:]
    return rows, cols, [int(count) for count in countsRequired]

def placeInGrid(grid, shape, startRow, startCol, availableSquares):
    
    shapeHeight = len(shape)
    shapeWidth = len(shape[0])

    if (startRow + shapeHeight) > len(grid):
        # print("rows too big!")
        return None, copy.copy(availableSquares)
    
    if (startCol + shapeWidth) > len(grid[0]):
        # print('cols too big!')
        return None, copy.copy(availableSquares)
    
    usedSpots = []
    for row in range(0, shapeHeight):
        for col in range(0, shapeWidth):
            shapeChar = shape[row][col]
            gridChar = grid[row + startRow][col + startCol]
            if gridChar == "#" and shapeChar == "#":
                return None, copy.copy(availableSquares)
            elif gridChar == "#" and shapeChar == ".":
                pass
            elif gridChar == "." and shapeChar == "#":
                usedSpots.append((row + startRow, col+startCol))
            else:
                pass

    newGrid = copy.deepcopy(grid)
    newAvailableSquares = copy.deepcopy(availableSquares)
    for spot in usedSpots:
        newAvailableSquares.remove(spot)
        row, col = spot
        newGrid[row][col] = "#"
    
    return newGrid, newAvailableSquares

NUMROWS = 6
NUMCOLS = 3
GRID = [["." for _ in range(0, NUMCOLS)] for _ in range(0, NUMROWS)]

AVAILABLE_SQUARES = set([(row, col) for row in range(0, NUMROWS) for col in range(0, NUMCOLS)])


def shapeSize(shape):
    return sum((row.count("#") for row in shape))

def bestPlacements(shapeMap, grid, placementCounts, availableSquares, memo):


    memoKey = (frozenset(availableSquares), tuple(sorted(placementCounts.items())))
    
    
    if memoKey in memo:
        # print("using memo!")
        # print(memoKey)
        # input("enter to con")
        return memo[memoKey]
    # input("enter to con")
    
    placements = []
    counts = []
    placementFound = False
    for shape, shapeIndex in shapeMap.items():
        if shapeSize(shape) > len(availableSquares):
            continue
        
        for square in availableSquares:
            row, col = square
            newGrid, newAvailableSquares = placeInGrid(grid, shape, row, col, availableSquares)
            if newGrid is None:
                continue
            placementFound = True
            newPlacementCounts = copy.copy(placementCounts)
            newPlacementCounts[shapeIndex] += 1

            recPlacements, recCounts = bestPlacements(shapeMap, newGrid, newPlacementCounts, newAvailableSquares, memo)
            placements += recPlacements
            counts += recCounts
    
    if not(placementFound):
        # print("grid:")
        # for row in grid:
        #     print(row)
        # print("placementCounts:", placementCounts)
        # input("base case. enter to con")
        # print()
        ans = [grid], [placementCounts]
        memo[memoKey] = ans
        return ans


    # print("grid:")
    # for row in grid:
    #     print(row)

    # print("returning:")
    # print("len(placements):", len(placements))
    # for p in placements:
    #     for row in p:
    #         print(row)
    #     print()
    # print("len(counts):", len(counts))
    # for c in counts:
    #     print(c)
    
    # input("recursive case. enter to con")
    # print()
    ans = placements, counts
    memo[memoKey] = ans
    return ans
        


def bestPlacementsWrapper(shapeMap, numRows, numCols):
    fullShapeMap = {}
    for index, shape in shapeMap.items():
        fullShapeMap[tuple(shape)] = index
        # print(shape)
        
        # input("enter to rotate")
        fullShapeMap[tuple(rotateShape(shape))] = index
        fullShapeMap[tuple(rotateShape(rotateShape(shape)))] = index
        fullShapeMap[tuple(rotateShape(rotateShape(rotateShape(shape))))] = index
        
    
    
    grid = [["." for _ in range(numCols)] for _ in range(0, numRows)]
    placementCounts = {shape:0 for shape in shapeMap}
    availableSquares = set([(row, col) for row in range(0, numRows) for col in range(0, numCols)])
    # print("numRows:", numRows)
    # print("numCols:", numCols)
    finalPlacements, finalCounts = bestPlacements(fullShapeMap, grid, placementCounts, availableSquares, memo = {})
    # print("ans:", ans)
    # input("ans should be complex, enter to con...")
    return finalPlacements, finalCounts


def findPlacements(shapes):
    print("shapes:", shapes)
    ans = {}
    for row in range(0, 5):
        for col in range(0, 5):
            key = (row, col)
            ans[key] = bestPlacementsWrapper(shapes, row, col)
    return ans


def rotateShape(shape):
    return tuple(tuple(shape[col][row] for col in reversed(range(0, len(shape)))) for row in range(0, len(shape[0])))

ACTUAL_PLACEMENTS, COUNTS = bestPlacementsWrapper(shapeMapping, 6,4)
print("len(ACTUAL_PLACEMENTS):", len(ACTUAL_PLACEMENTS))
PAIRS = list(zip(ACTUAL_PLACEMENTS, COUNTS))
SORTED_PAIRS = sorted(PAIRS,
    key = lambda PAIR: sum(PAIR[1].values()),
    reverse=True
)

for p, c in SORTED_PAIRS:
    for row in p:
        print(row)
    for k,v in c.items():
        print(k,"|",v)
    input("enter to con")
