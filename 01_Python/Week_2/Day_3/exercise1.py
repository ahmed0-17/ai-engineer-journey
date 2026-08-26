class FileLogger:


     def __init__(self,filename):
        self.filename=filename
     def __enter__(self):
      self.file=open(self.filename,"a")
      print("File open")
      return self
     

     def log(self,msg):
       self.file.write(msg + "\n")


     def __exit__(self,exc_type,exc_value,traceback):
      if exc_type is not None :
         print (exc_type," : ", exc_value)
      self.file.close()
      print("File closed")
      return False

  


with FileLogger("app.txt") as logger:
    logger.log("Application started")
    logger.log("Processing data")
    raise ValueError("Value error")


 