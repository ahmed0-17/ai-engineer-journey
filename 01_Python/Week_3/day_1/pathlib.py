from pathlib import Path

documents = Path("data/documents")

for file in documents.glob("*.txt"):
    print(file)