f_name = "3_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

def calcBest(L, budget):
    if budget == len(L):
        return int(L)

    if budget > len(L):
        return -1

    if budget == 1:
        return max([int(char) for char in L])

    for i in range(9, 0, -1):
        i_str = str(i)
        if i_str not in L:
            continue
        startIndex = L.index(i_str)
        # print("L:             ", L)
        # print("L[startIndex:]:", L[startIndex+1:])
        # input("enter to con")
        subSol = calcBest(L[startIndex+1:], budget-1)
        if subSol != -1:
            return int(str(L[startIndex]) + str(subSol))

    
    return ans


def getHighest(line):
    clean_line = line.replace("\n", "")
    # print("clean_line:", clean_line)
    ans = calcBest(clean_line, 12)
    # print("ans:", ans)
    # print()
    return ans



values = [int(getHighest(line)) for line in lines]
print(sum(values))