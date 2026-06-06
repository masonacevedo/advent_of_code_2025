import copy
from collections import deque
import time

# DATA PROCESSING

f_name = "10_input.txt"
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

def simulatePresses(numArray, button, k):
    ans = copy.copy(numArray)
    for slot in button:
        ans[slot] += k
    return ans


def getFullyDetermined(start, target, button, otherButtons):
    # returns true if the given button is fully determined,
    # i.e. is the only button that hits a certain slot.
    slots_hit = button

    for slot in slots_hit:
        otherButtonsHit = [not(slot in b) for b in otherButtons]
        if all(otherButtonsHit):
            return True, slot
    return False, None

def mostDetermined(start, target, buttonArray):
    # given the array of buttons, and knowing that none of them
    # are fully determined, we return the button s.t.
    # it has the smallest possible range. 
    
    hitsNeeded = [slotEnd - slotStart for slotEnd, slotStart in zip(target, start)]
    upperBounds = []
    for b in buttonArray:
        
        maxHits = [hitsNeeded[slot] for slot in b]
        upperBounds.append(min(maxHits))
    
    bestIndex = upperBounds.index(min(upperBounds))
    return buttonArray[bestIndex], upperBounds[bestIndex]


def getBestButton(startConfig, targetConfig, buttonArray):
    for button in buttonArray:
        otherButtons = [b for b in buttonArray if b != button]
        fullyDetermined, slot = getFullyDetermined(startConfig, targetConfig, button, otherButtons)
        if fullyDetermined:
            return button, True, slot, None
    bestButton, numPresses = mostDetermined(startConfig, targetConfig, buttonArray)
    return bestButton, False, None, numPresses
        


def minPresses(startConfig, targetConfig, allButtons, level, memo, invalidButtons):

    memoKey = (tuple(invalidButtons), tuple(startConfig))
    buttonArray = [allButtons[i] for i in range(0, len(allButtons)) if i not in invalidButtons]
    # print("memoKey:", memoKey)
    # input("enter to con")
    if memoKey in memo:
        print("using memo!", memoKey)
        return memo[memoKey]

    if len(buttonArray) == 1:
        hitsNeeded = [slotEnd - slotStart for slotEnd, slotStart in zip(targetConfig, startConfig)]
        k = max(hitsNeeded)
        if k < 0:
            return float('inf')
        if simulatePresses(startConfig, buttonArray[0], k) != targetConfig:
            return float('inf')
        return k
    bestButton, fullyDetermined, slot, upperBoundPresses = getBestButton(startConfig, targetConfig, buttonArray)
    newInvalidIndex = allButtons.index(bestButton)
    # print("allButtons: ", allButtons)
    # print("invalidButtons:", invalidButtons)
    # print("buttonArray:", buttonArray)

    # print("bestButton: ", bestButton)
    # print("newInvalidIndex:", newInvalidIndex)
    # input("enter to con")
    # print()
    if fullyDetermined:
        pressesRequired = targetConfig[slot] - startConfig[slot]
        if pressesRequired < 0:
            return float('inf')
        otherButtons = [b for b in buttonArray if b != bestButton]
        newConfig = simulatePresses(startConfig, bestButton, pressesRequired)
        larger = [s > t for s,t in zip(newConfig, targetConfig)]
        if any(larger):
            return float('inf')
        ans = pressesRequired + minPresses(newConfig, targetConfig, allButtons, level+1, memo, invalidButtons=invalidButtons+[newInvalidIndex])
        memo[memoKey] = ans
        return ans

    options = []
    for numPresses in range(upperBoundPresses, -1, -1):
        start = simulatePresses(startConfig, bestButton, numPresses)
        # print("buttonArray:", buttonArray)
        # input()
        # otherButtons = [b for b in buttonArray if b != bestButton]
        ans = numPresses + minPresses(start, targetConfig, allButtons, level+1, memo, invalidButtons=invalidButtons+[newInvalidIndex])
        options.append(ans)
    result = min(options)
    memo[memoKey] = result
    return result


def minPressesWrapper(targetConfig, buttonArray):
    return minPresses([0]*len(targetConfig), targetConfig, buttonArray, level=0, memo={}, invalidButtons=[])

    

# FINAL LOOP

presses = []
for i, line in enumerate(clean_lines):
    lastPrint = time.time()
    if time.time() - lastPrint > 1:
        lastPrint = time.time()
        print(i,"/", len(clean_lines))

    configString, *buttons, joltageString = line.split(" ")
    targetConfig = stringToBoolArray(configString)

    joltages = stringToNumArray(joltageString)
    buttonArray = [stringToButton(button) for button in buttons]
    print("joltages:", joltages)
    print("buttonArray:", buttonArray)
    print()
    ans = minPressesWrapper(joltages, buttonArray)
    print("ans:", ans)
    print("\n")
    presses.append(ans)

print("presses:", presses)
print("sum(presses):", sum(presses))