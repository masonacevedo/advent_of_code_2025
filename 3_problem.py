f_name = "3_example.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

def calcBest(L):
    if len(L) == 12:
        return L
    
    # print("L:", L)
    possibilities = []
    for i in range(0, len(L)):
        s = L[0:i] + L[i+1:]
        possibilities.append(int(calcBest(s)))
    
    return str(max(possibilities))


def getHighest(line):
    clean_line = line.replace("\n", "")
    # print("clean_line:", clean_line)
    ans = calcBest(clean_line)
    # print("ans:", ans)
    # print()
    return ans



values = [int(getHighest(line)) for line in lines]
print(sum(values))