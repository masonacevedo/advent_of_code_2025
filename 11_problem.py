# thought: if the path is doomed. i.e. impossible for this path to reach out
# while having both svr and fft on it, then we should stop branching out and
# return 0 early. the question is, how do we do that... 
# thought: is there an easy way to determine this? or a moderately expensive way even? 
#   thought: before we do the real path search, we compute: 
#            for each node, how many paths are there from this path to
#
# thought: if i'm looking for all paths from FOO to BAR, I could cound them naively.
#          HOWEVER, I could also count all paths from FOO to INT, and from INT to BAR.
#          If there's 8 paths from FOO to INT, and 9 paths from INT to BAR, then
#          I know there's 72 paths overall!! 
import math
import copy

f_name = "11_input.txt"
with open(f_name, "r+") as f:
    lines = f.readlines()


clean_lines = [line.replace("\n", "") for line in lines]

adjList = {}
for line in clean_lines:
    node, *neighbors = line.split(" ")
    node = node[0:-1]
    adjList[node] = neighbors

adjList['out'] = []

for k,v in adjList.items():
    print(k,"|",v)
print()

def findPaths(source, dest, adjList, currentPath = set(), memo={}):

    memoKey = (source, dest, frozenset(currentPath))
    if memoKey in memo:
        return memo[memoKey]

    if source == dest:
        return 1
    
    if source in currentPath:
        return 0
    
    currentPath.add(source)
    count = 0
    for neighbor in adjList[source]:
        pathsFromNeighbor = findPaths(neighbor, dest, adjList, currentPath, memo)
        count += pathsFromNeighbor
        if pathsFromNeighbor is None:
            continue

    currentPath.remove(source)
    memo[memoKey] = count
    return count


svr2dacPaths = findPaths("svr", "dac", adjList)
print('1')
dac2fftPaths = findPaths("dac", "fft", adjList)
print('2')
fft2outPaths = findPaths("fft", "out", adjList)
print('3')

route1Paths = [svr2dacPaths, dac2fftPaths, fft2outPaths]
route1 = math.prod(route1Paths)


print("route1Paths:", route1Paths)


svr2fftPaths = findPaths("svr", "fft", adjList)
print('4')
fft2dacPaths = findPaths("fft", "dac", adjList)
print('5')
dac2outPaths = findPaths("dac", "out", adjList)
print('6')

route2Paths = [svr2fftPaths, fft2dacPaths, dac2outPaths]
route2 = math.prod(route2Paths)

print("route2Paths:", route2Paths)

print("ans:", route1 + route2)