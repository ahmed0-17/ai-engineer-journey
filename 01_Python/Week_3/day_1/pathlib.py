from pathlib import Path

documents = Path("data/documents")

for file in documents.glob("*.txt"):
    print(file)






path = Path("documents")

if path.exists():
    if path.is_dir():
        print("This is a folder")
    elif path.is_file():
        print("This is a file")
else:
    print("Path does not exist")    