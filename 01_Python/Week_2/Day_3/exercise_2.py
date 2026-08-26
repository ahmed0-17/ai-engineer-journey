class FileManager:

    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        print("File opened")
        return self    

    def write(self,msg):
        self.file.write(msg)

    def read(self):
      return  self.file.read()

    def append(self,msg):
        self.file.write("\n"+msg)

           


    def __exit__(self,exc_type,exc_value,traceback):
        if exc_type is not None:
            print("Error type : ", exc_type)  

        self.file.close()
        print("File closed")
        return False


with FileManager("app.txt","r") as fm:

  print(fm.read())
  
#   fm.write("Hello AI Engineer")
  raise ValueError("Value Error")


print("Program coninues")