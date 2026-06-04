f_name = "5_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()



clean_lines = [line.replace("\n", "") for line in lines]
midpoint = clean_lines.index("")

print()



def mergeSortedIntervals(leftInterval, rightInterval):
    # print("leftInterval:", leftInterval)
    if leftInterval[1] < rightInterval[0]:
        return [leftInterval, rightInterval]
    return [[leftInterval[0], max(leftInterval[1], rightInterval[1])]]


freshRanges = clean_lines[0:midpoint]
intervals = []
for rangeString in freshRanges:
    left, right = rangeString.split("-")
    intervals.append([int(left), int(right)])


sortedIntervals = sorted(intervals, key = lambda i: i[0])
# print(sortedIntervals)
i = 0
while i < len(sortedIntervals)-1:
    merge = mergeSortedIntervals(sortedIntervals[i], sortedIntervals[i+1])
    if len(merge) == 2:
        i += 1
        continue
    sortedIntervals[i] = merge[0]
    del sortedIntervals[i+1]

# for i in sortedIntervals:
#     print(i)

def freshCount(interval):
    return interval[1] - interval[0] + 1

print(sum([freshCount(i) for i in sortedIntervals]))