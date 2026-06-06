import copy
from collections import deque

# DATA PROCESSING

f_name = "10_example.txt"
with open(f_name, "r+") as f:
    lines = f.readlines()


clean_lines = [line.replace("\n", "") for line in lines]


def stringToBoolArray(s):
    ans = []
    for char in s[1:-1]:
        if char == ".":
            ans.append(False)
        elif char == "#":
            ans.append(True)
        else:
            raise Exception("invalid input!")
    return ans

def stringToNumArray(s):
    a = s.replace("{","")
    a = a.replace("}","")
    numsAsStrs = a.split(",")
    return [int(s) for s in numsAsStrs]


def stringToButton(s):
    a = s.replace("(","")
    a = a.replace(")","")
    buttonStrings = a.split(",")
    return [int(x) for x in buttonStrings]

# LOGIC

def simulatePress(numArray, button):
    ans = copy.copy(numArray)
    for i in button:
        ans[i] += 1
    return ans

def getNeighbors(numArray, buttonArray):
    return [simulatePress(numArray, button) for button in buttonArray]

def minPresses(startingConfig, targetConfig, buttonArray):
    queue = deque([(startingConfig, 0)])
    seenBefore = set()

    while len(queue) > 0:
        currentConfig, level = queue.popleft()
        # print("currentConfig:", currentConfig)
        # print("level:", level)
        # input("enter to con")
        if tuple(currentConfig) in seenBefore:
            continue
        
        if currentConfig == targetConfig:
            return level

        neighbors = getNeighbors(currentConfig, buttonArray)

        for n in neighbors:
            queue.append((n, level+1))

        seenBefore.add(tuple(currentConfig))



def minPressesWrapper(targetConfig, buttonArray):
    return minPresses([0]*len(targetConfig), targetConfig, buttonArray)

    

# FINAL LOOP

presses = []
for line in clean_lines:
    configString, *buttons, joltageString = line.split(" ")
    targetConfig = stringToBoolArray(configString)

    joltages = stringToNumArray(joltageString)
    buttonArray = [stringToButton(button) for button in buttons]
    
    ans = minPressesWrapper(joltages, buttonArray)
    presses.append(ans)

print("presses:", presses)
print("sum(presses):", sum(presses))