f_name = "2_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()
# print("lines:", lines)
ranges = lines[0].split(",")


def chopWorks(s, i):
    # return true if s is just the first i characters
    # repeated some number of times, false otherwise.
    # print("i:", i)
    # print("s:", s)
    prefix = s[0:i]
    # print("prefix:", prefix)
    # print("prefix*i:", prefix * (len(s)//i))
    answer = (s == prefix * (len(s)//i))
    # print('answer:', answer)
    # input("enter to con")
    return answer

def invalid(num):
    s = str(num)
    for i in range(1, (len(s)//2)+1):
        if chopWorks(s, i):
            # print("s:", s)
            # print("i:", i)
            # input('enter to con')
            return True
    return False

invalid_IDs = []
for r in ranges:
    # print("r:", r)
    start, end = r.split("-")

    for i in range(int(start), int(end)+1):
        if invalid(i):
            invalid_IDs.append(i)
    
    # input("enter to con")


print(sum(invalid_IDs))