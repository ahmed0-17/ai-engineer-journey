from pathlib import Path


dir= Path("01_Python/Week_3/Day_1/Data")
dir.mkdir(exist_ok=True,parents=True)
file_path= dir / "data.txt"
file_path.touch()
file_path.write_text("Hello AI Engineer")


print("Path:", file_path)                 #returns the file_path
print("Exists:", file_path.exists())      #exists check wether path exists or not
print("Name:", file_path.name)            #name returns the name of the file
print("Extension:", file_path.suffix)     #suffix returns the file extention
print("Parent:", file_path.parent)        #parent gives the parent directory of file
print("Content:", file_path.read_text())  #read_text reads the content of file