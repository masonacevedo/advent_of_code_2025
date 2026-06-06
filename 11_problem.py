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

def findPaths(source, dest, adjList, currentPath = set()):
    if source == dest:
        return 1
    
    if source in currentPath:
        return 0
    
    currentPath.add(source)
    count = 0
    for neighbor in adjList[source]:
        pathsFromNeighbor = findPaths(neighbor, dest, adjList, currentPath)
        count += pathsFromNeighbor
        if pathsFromNeighbor is None:
            continue

    currentPath.remove(source)
    return count
    
ans = findPaths("you", "out", adjList)
print("ans:", ans)
