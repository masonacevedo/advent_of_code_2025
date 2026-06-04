f_name = "3_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

def getHighest(line):
    # print("line:", line)
    clean_line = line.replace("\n", "")
    bestSoFar = float('-inf')
    for i in range(0, len(clean_line)):
        for j in range(i+1, len(clean_line)):
            leftNum = line[i]
            rightNum = line[j]
            num = 10*int(leftNum) + int(rightNum)
            bestSoFar = max(num, bestSoFar)
    
    # print("bestSoFar:", bestSoFar)
    # print()
    return bestSoFar

values = [getHighest(line) for line in lines]
print(sum(values))