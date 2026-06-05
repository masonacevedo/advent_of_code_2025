import time
f_name = "9_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

clean_lines = [line.replace("\n", "") for line in lines]

coordStrings = [s.split(",") for s in clean_lines]
coordNums = list(
                map(
                    lambda L: list(int(e) for e in L),
                    coordStrings
                )
            )


def getGreens(coords):
    greens = set()
    
    for i in range(0, len(coords)):
        if i == len(coords)-1:
            x1, y1 = coords[i]
            x2, y2 = coords[0]
        else:
            x1, y1 = coords[i]
            x2, y2 = coords[i+1]
        
        if y2 == y1:
            lower, upper = min(x1, x2), max(x1, x2)
            for xVal in range(lower, upper+1):
                greens.add((xVal, y1))
        elif x1 == x2:
            lower, upper = min(y1, y2), max(y1, y2)
            for yVal in range(lower, upper+1):
                greens.add((x1, yVal))
        else:
            raise Exception("Invalid input")
        
    return greens


def isInside(corner1, corner2, candidate):
    # returns true if the candidate 
    # is inside the rectangle defined by 
    # corner1 and corner2

    x1, y1 = corner1
    x2, y2 = corner2
    canX, canY = candidate

    return (min(x1, x2) < canX) and (canX < max(x1, x2)) and (min(y1, y2) < canY) and (canY < max(y1, y2))

greens = getGreens(coordNums)

def hasAnyGreens(corner1, corner2):
    for g in greens:
        if isInside(corner1, corner2, g):
            return True
    return False

def maxArea(coords):
    bestSoFar = float('-inf')
    count = 0
    numPairs = (len(coords) * (len(coords)-1))//2
    print("numPairs:", numPairs)
    lastPrint = time.time()

    for i in range(0, len(coords)):
        for j in range(i+1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            
            area = (abs(y2-y1)+1)*(abs(x1-x2)+1)
            if not(hasAnyGreens(coords[i], coords[j])):
                # print("none found inside!")
                bestSoFar = max(area, bestSoFar)
            count += 1
            
            if (time.time() - lastPrint) > 10:
                lastPrint = time.time()
                print("count:   ", count)
                print("numPairs:", numPairs)
            
            
    return bestSoFar

print(maxArea(coordNums))