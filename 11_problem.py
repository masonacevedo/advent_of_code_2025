# Algorithm:
#     def ChokepointCount(source, target):
#           identify one path from source to target.
#           starting from the middle node:
#               determine if this node is a chokpoint.
#               if it is, recursively chokepoint count the number
#               of paths from source to the chokpoint, and also from
#               the chokepoint to the source. 
#               multiply these for the answer.
#           if there are no chokepoints, then resort to a brute force
#           enumeration. 
#     def isChokepoint(source, target, candidate):
#       remove candidate from adjList
#       check if there's a path from source to target.
#       if there is, return True.
#       otherwise, returen False
import math
import copy

f_name = "11_input.txt"
with open(f_name, "r+") as f:
    lines = f.readlines()


clean_lines = [line.replace("\n", "") for line in lines]

ADJACENCY_LIST = {}
for line in clean_lines:
    node, *neighbors = line.split(" ")
    node = node[0:-1]
    ADJACENCY_LIST[node] = neighbors

ADJACENCY_LIST['out'] = []

def findPath(source, dest, adjList, currentPath = None):
    if source not in adjList:
        return None
    if currentPath is None:
        currentPath = set()

    if dest in adjList[source]:
        return [source, dest]
    
    if source in currentPath:
        return None
    
    currentPath.add(source)

    for neighbor in adjList[source]:
        p = findPath(neighbor, dest, adjList)
        if p is not None:
            return [source] + p

    return None


def pathExists(source, dest, adjList):
    path = findPath(source, dest, adjList)
    if path is None:
        return False
    else:
        return True


def isChokepoint(candidate, source, dest, adjList):
    withCandidate = pathExists(source, dest, adjList)
    savedNeighbors = adjList[candidate]

    del adjList[candidate]
    woutCandidate = pathExists(source, dest, adjList)
    adjList[candidate] = savedNeighbors

    return (withCandidate and not(woutCandidate))


def rotateOrder(L):
    n = len(L)
    midPoint = n//2
    yield L[midPoint]
    for i in range(1, midPoint+1):
        yield L[midPoint - i]
        if midPoint + i >= n:
            return
        yield L[midPoint + i]


def countPathsNaive(source, dest, adjList, currentPath = None, memo = None):
    if currentPath is None:
        currentPath = set()
    if memo is None:
        memo = {}

    memoKey = (source, dest, frozenset(currentPath))
    if memoKey in memo:
        print("using memo!")
        return memo[memoKey]

    if source == dest:
        return 1

    if source in currentPath:
        return 0

    currentPath.add(source)
    count = 0
    for neighbor in adjList[source]:
        pathsFromNeighbor = countPathsNaive(neighbor, dest, adjList, currentPath, memo)
        count += pathsFromNeighbor
        
    currentPath.remove(source)
    memo[memoKey] = count
    return count

# def countPaths(source, dest, adjList):
#     path = findPath(source, dest, adjList)
#     if path is None:
#         return 0

#     # don't need the source and dest node
#     # on the actual path.
#     del path[0]
#     del path[-1]

#     print("path:", path)
    
#     rotatedNodes = list(rotateOrder(path))
#     print("path:", path)
#     print("rotatedNodes:", rotatedNodes)
    
#     for node in rotatedNodes:
#         if isChokepoint(node, source, dest, adjList):
#             print("chokePoint found!")
#             pass
    
#     input("enter to con")
    
    # if no chokepoints are found, return the brute force path count! 

ans = countPathsNaive("you", "out", ADJACENCY_LIST)
print("ans:", ans)





# svr2dacPaths = findPaths("you", "hho", adjList)
# print('1')
# dac2fftPaths = findPaths("hho", "nhm", adjList)
# print('2')
# fft2outPaths = findPaths("nhm", "out", adjList)
# print('3')

# route1Paths = [svr2dacPaths, dac2fftPaths, fft2outPaths]
# route1 = math.prod(route1Paths)

