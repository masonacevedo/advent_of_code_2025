f_name = "2_input.txt"

with open(f_name, "r+") as f:
    lines = f.readlines()
# print("lines:", lines)
ranges = lines[0].split(",")



def invalid(num):
    s = str(num)
    if len(s) % 2 == 1:
        return False
    
    leftHalf = s[0:len(s)//2]
    rightHalf = s[len(s)//2:]
    return leftHalf == rightHalf

invalid_IDs = []
for r in ranges:
    # print("r:", r)
    start, end = r.split("-")

    for i in range(int(start), int(end)+1):
        if invalid(i):
            invalid_IDs.append(i)
    
    # input("enter to con")


print(sum(invalid_IDs))