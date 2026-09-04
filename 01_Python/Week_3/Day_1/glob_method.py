from pathlib import Path

folder=Path("01_Python/Week_3/Day_1/Data")

# files=folder.glob("*.txt")
# files = folder.glob("*.py")
# files=folder.glob("*.json")
files = folder.glob("data*.txt")

for file in files:
    print(file)




#list with glob

files = list(folder.glob("*.txt"))

print(files)    