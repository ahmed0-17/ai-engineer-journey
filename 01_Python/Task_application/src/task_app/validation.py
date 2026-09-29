class Validation:

    @staticmethod
    def validate_title(title:str)->bool:
        if(title.strip==""):return False
        return True

    @staticmethod 
    def validate_description(description:str)->bool:
        if(description.strip()==""):return False
        return True    

    @staticmethod
    def validate_priority(priority:str)->bool:    
         if priority in ("High","Medium","Low"): return True
         return False 

    @staticmethod
    def validate_id(task_id:int)->bool:
        if(task_id<=0): return False 
        return True    