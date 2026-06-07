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


def countPathsNaive(source, dest, adjList, currentPath = None):
    # print("source:", source)
    # print("dest:  ", dest)
    # print("currentPath:", currentPath)
    # input("enter to con")
    if currentPath is None:
        currentPath = set()

    if source == dest:
        return 1

    if source in currentPath:
        return 0

    currentPath.add(source)
    count = 0
    for neighbor in adjList[source]:
        pathsFromNeighbor = countPathsNaive(neighbor, dest, adjList, currentPath)
        count += pathsFromNeighbor
        
    currentPath.remove(source)
    return count

def countPaths(source, dest, adjList):
    print("source:", source)
    print("dest:  ", dest)

    print("finding one path...")
    path = findPath(source, dest, adjList)
    print("path found")
    if path is None:
        return 0

    # don't need the source and dest node
    # on the actual path.
    del path[0]
    del path[-1]
    if len(path) == 0:
        print("naive counting..")
        return countPathsNaive(source, dest, adjList)
    # print("source:", source)
    # print("dest:  ", dest)
    # print("len(path):", len(path))
    # print()
    # input("enter to con")
    rotatedNodes = list(rotateOrder(path))
    print("nodes rotated")
    for node in rotatedNodes:
        print("looking at node:", node)
        if isChokepoint(node, source, dest, adjList):
            print("source:     ", source)
            print("dest:       ", dest)
            print("chokePoint: ", node)
            print("chokepoint found!")
            input("enter to continue")
            print()
            firstHalf = countPaths(source, node, adjList)
            secondHalf = countPaths(node, dest, adjList)
            return firstHalf*secondHalf
    
    print("naive counting...")
    return countPathsNaive(source, dest, adjList)


def findCycle(adjList):
    startNode = "svr"
    return topSort(adjList, startNode, visited = set(), currentPath = [])


def topSort(adjList, currentNode, visited, currentPath):

    if currentNode in currentPath:
        return currentPath + [currentNode]

    if currentNode in visited:
        return None

    currentPath.append(currentNode)

    for neighbor in adjList[currentNode]:
        result = topSort(adjList, neighbor, visited, currentPath)
        if result:
            return result

    currentPath.remove(currentNode)

    visited.add(currentNode)
    return None


print(findCycle(ADJACENCY_LIST))


# svr2dacPaths = countPaths("svr", "dac", ADJACENCY_LIST)
# print('1 progress')
# dac2fftPaths = countPaths("dac", "fft", ADJACENCY_LIST)
# print('2 progress')
# fft2outPaths = countPaths("fft", "out", ADJACENCY_LIST)
# print('3 progress')

# route1Paths = [svr2dacPaths, dac2fftPaths, fft2outPaths]
# route1Product = math.prod(route1Paths)
# print("route1Paths:", route1Paths)


# ans = svr2fftPaths = countPaths("dac", "out", ADJACENCY_LIST)
# print("ans:", ans)
# print('4 progress')
# fft2dacPaths = countPaths("fft", "dac", ADJACENCY_LIST)
# print('5 progress')
# dac2outPaths = countPaths("dac", "out", ADJACENCY_LIST)

# route2Paths = [svr2fftPaths, fft2dacPaths, dac2outPaths]
# route2Product = math.prod(route2Paths)
# print("route2Paths:", route2Paths)

# print("ans:", route1Product + route2Product)