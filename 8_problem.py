import math
from union_find import UnionFind

f_name = "8_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

raw_coords = [l.replace("\n", "") for l in lines]
# print(raw_coords)

def distance(c1, c2):
    return math.sqrt(sum([(a - b)**2 for a,b in zip(c1, c2)]))


def pairsAndDistances(coords):
    ans = []
    for i in range(0, len(coords)):
        for j in range(i+1, len(coords)):
            ans.append([coords[i], coords[j], distance(coords[i], coords[j])])
    
    return sorted(ans, key = lambda t: t[2])

def rawCoordToNum(rawCoord):
    x, y, z = rawCoord.split(",")
    return [int(x), int(y), int(z)]
coordNums = [rawCoordToNum(rawCoord) for rawCoord in raw_coords]

sortedTriplets = pairsAndDistances(coordNums)
# for t in sortedTriplets[0:10]:
#     print(t)



uf = UnionFind(elements = raw_coords)

# print("raw_coords:", raw_coords)

def connect(triplet):
    coord1, coord2, distance = triplet
    c1str = "".join([str(x) + "," for x in coord1])
    c1str = c1str[0:-1]


    c2str = "".join([str(x) + "," for x in coord2])
    c2str = c2str[0:-1]
    
    if uf.connected(c1str, c2str):
        return
    
    # print("before")
    # print(uf.component_sizes())
    uf.union(c1str, c2str)
    # print("after")
    # print(uf.component_sizes())

    # input("enter to con")

NUM_CONNECTIONS = 1000
for i in range(0, NUM_CONNECTIONS):
    connect(sortedTriplets[i])

print(uf.component_sizes())

componentSizes = sorted(uf.component_sizes().values())

ans = componentSizes[-1] * componentSizes[-2] * componentSizes[-3]
print("ans:", ans)

# def connectClosest(coords):
#     bestSoFar = float('inf')
#     for i in range(0, len(coords)):
#         for j in range(i+1, len(coords)):

#             if distance(coords[i], coords[j]) < bestSoFar:
#                 bestSoFar = distance(coords[i], coords[j])
#                 coord1 = coords[i]
#                 coord2 = coords[j]
    
#     if coord1 in adjList[tuple(coord2)]:
#         print("returning")
#         return

#     print('changing circuit sizes!')
#     newCircuitSize = circuitSizes[tuple(coord1)] + circuitSizes[tuple(coord2)]
#     circuitSizes[tuple(coord1)] = newCircuitSize
#     circuitSizes[tuple(coord2)] = newCircuitSize
    

#     adjList[tuple(coord1)].append(coord2)
#     adjList[tuple(coord2)].append(coord1)
    
    
