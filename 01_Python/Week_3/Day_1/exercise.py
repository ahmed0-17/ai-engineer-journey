from pathlib import Path


dir= Path("01_Python/Week_3/Day_1/documents")
dir2= Path("01_Python/Week_3/Day_1/research")
dir.mkdir(exist_ok=True,parents=True)
dir2.mkdir(exist_ok=True,parents=True)
files=["Python.txt","rag.txt","agents.txt","ai.txt","backend.txt","data.json","notes.pdf"]
for file in files:
 if file in ("rag.txt","agents.txt"):
  file_path= dir2 / file
  file_path.write_text("Hello AI Engineer")
 else:
  file_path= dir / file
  file_path.write_text("Hello AI Engineer")



#listing files with .txt extension
for file in dir.glob("*.txt"):
    print(file)