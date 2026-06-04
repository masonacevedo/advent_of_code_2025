import sys
import subprocess

if __name__ == "__main__":
    number_string = sys.argv[1]
    number = int(number_string)
    file_name_1 = f"{number}_example.txt"
    file_name_2 = f"{number}_input.txt"
    file_name_3 = f"{number}_problem.py"

    fileNames = [file_name_1,file_name_2,file_name_3]

    for name in fileNames:
        print(name)
        subprocess.run(["touch", name])
