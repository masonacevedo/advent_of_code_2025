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

f_name = "11_example.txt"
with open(f_name, "r+") as f:
    lines = f.readlines()


clean_lines = [line.replace("\n", "") for line in lines]

ADJACENCY_LIST = {}
for line in clean_lines:
    node, *neighbors = line.split(" ")
    node = node[0:-1]
    ADJACENCY_LIST[node] = neighbors

ADJACENCY_LIST['out'] = []

def findPath(source, dest, adjList, currentPath = set()):

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


# def isChokepoint(candidate, source, dest, adjList):
#     withCandidate = pathExists(source, dest, adjList)
#     savedNeighbors = adjList[candidate]

#     del adjList[candidate]
#     woutCandidate = pathExists(source, dest, adjList)
#     adjList[candidate] = savedNeighbors

#     return (withCandidate and not(woutCandidate))


for k,v in ADJACENCY_LIST.items():
    print(k,"|",v)
print()
p = pathExists("you", "out", ADJACENCY_LIST)
print("p:", p)
del ADJACENCY_LIST["bbb"]

for k,v in ADJACENCY_LIST.items():
    print(k,"|",v)
print()
p = pathExists("you", "out", ADJACENCY_LIST)
print("p:", p)

# ans = isChokepoint("bbb", "you", "out", ADJACENCY_LIST)

# def findPaths(source, dest, adjList, currentPath = set(), memo={}):

#     memoKey = (source, dest, frozenset(currentPath))
#     if memoKey in memo:
#         return memo[memoKey]

#     if source == dest:
#         return 1

#     if source in currentPath:
#         return 0

#     currentPath.add(source)
#     count = 0
#     for neighbor in adjList[source]:
#         pathsFromNeighbor = findPaths(neighbor, dest, adjList, currentPath, memo)
#         count += pathsFromNeighbor
#         if pathsFromNeighbor is None:
#             continue

#     currentPath.remove(source)
#     memo[memoKey] = count
#     return count



# svr2dacPaths = findPaths("you", "hho", adjList)
# print('1')
# dac2fftPaths = findPaths("hho", "nhm", adjList)
# print('2')
# fft2outPaths = findPaths("nhm", "out", adjList)
# print('3')

# route1Paths = [svr2dacPaths, dac2fftPaths, fft2outPaths]
# route1 = math.prod(route1Paths)

