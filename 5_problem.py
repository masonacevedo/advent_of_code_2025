f_name = "5_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()



clean_lines = [line.replace("\n", "") for line in lines]
midpoint = clean_lines.index("")

print()
print()
print()

freshRanges = clean_lines[0:midpoint]

ings = clean_lines[midpoint+1:]

def isFresh(ing):
    for r in freshRanges:
        lower, upper = r.split("-")
        if int(lower) <= ing and ing <= int(upper):
            return True
    return False

freshIngs = [isFresh(int(ing)) for ing in ings]
print(sum(freshIngs))