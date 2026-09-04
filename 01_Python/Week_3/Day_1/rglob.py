from pathlib import Path

folder = Path("01_Python/Week_3/Day_1")

for file in folder.rglob("*.txt"):

    print("File:", file)
    print("Name:", file.name)
    print("Suffix:", file.suffix)
    print("Parent:", file.parent)
    print("Exist:",file.exists())