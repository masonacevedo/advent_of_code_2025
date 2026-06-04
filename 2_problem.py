f_name = "2_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()
ranges = lines[0].split(",")


def chopWorks(s, i):
    # return true if s is just the first i characters
    # repeated some number of times, false otherwise.
    prefix = s[0:i]
    answer = (s == prefix * (len(s)//i))
    return answer

def invalid(num):
    s = str(num)
    for i in range(1, (len(s)//2)+1):
        if chopWorks(s, i):
            return True
    return False

invalid_IDs = []
for r in ranges:
    start, end = r.split("-")

    for i in range(int(start), int(end)+1):
        if invalid(i):
            invalid_IDs.append(i)


print(sum(invalid_IDs))