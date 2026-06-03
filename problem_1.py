f_name = "1_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()

def processLine(line, currentNum):
    
    if "L" in line:
        numberStart = line.index("L")
    elif "R" in line:
        numberStart = line.index("R")
    
    number = int(line[numberStart+1:-1])
    
    if "L" in line:
        answer = (currentNum - number) % 100
    else:
        answer = (currentNum + number) % 100
    
    return answer

number = 50
seenValues = []
for line in lines:
    number = processLine(line, number)
    seenValues.append(number)

print("seenValues.count(0):", seenValues.count(0))