import math

f_name = "6_input.txt"

with open(f_name, "r+") as f:
    grid = f.readlines()

clean_lines = [line.replace("\n","") for line in grid]

for r in clean_lines:
    print(repr(r))

row = 0
col = len(clean_lines[0])-1
numStrings = [str(i) for i in range(0, 10)]

processedString = ""
for col in range(len(clean_lines[0]) - 1, -1, -1):
    for row in range(0, len(clean_lines)):
        tile = clean_lines[row][col]
        processedString += tile

print("processedString:", processedString)

def customSplit(s):
    current = ""
    ans = []
    for char in s:
        current += char
        if char in ["*", "+"]:
            ans.append(current)
            current = ""
    return ans

problems = customSplit(processedString)
solutions = []

def solveProblem(problem):
    print("problem:", problem)
    if "+" in problem:
        operation = "add"
    else:
        operation = "mult"
    problem = problem.replace("+", "")
    problem = problem.replace("*", "")
    
    parts = problem.split(" ")
    clean_parts = list(filter(lambda s: s != "", parts))
    
    nums = [int(p) for p in clean_parts]
    if operation == "add":
        return sum(nums)
    else:
        return math.prod(nums)

for problem in problems:
    solutions.append(solveProblem(problem))

print("solutions:", solutions)
print(sum(solutions))