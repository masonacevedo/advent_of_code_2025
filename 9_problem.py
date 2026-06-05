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


def maxArea(coords):
    bestSoFar = float('-inf')
    for i in range(0, len(coords)):
        for j in range(i+1, len(coords)):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            
            area = (abs(y2-y1)+1)*(abs(x1-x2)+1)
            # print("coords[i]:", coords[i])
            # print("coords[j]:", coords[j])
            # print("area:", area)
            # input("enter to con")

            bestSoFar = max(area, bestSoFar)
    return bestSoFar

print(maxArea(coordNums))