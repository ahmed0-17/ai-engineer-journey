import json


user={
    "name":"Ahmed Ali Malik",
    "contact":{
        "email":"ahmed5432@gmail.com",
        "phone": "+92234564322",
         },
    "projects":{
        "project1" :"AI Chatbot",
        "project2" :"Task Flow",

    }     

}


with open("user_info.json","w") as info:
      json.dump(user,info,indent=4)
with open("user_info.json","r") as info:
      user_data=json.load(info)
      print(user_data)
      print(user_data["contact"]["email"])
      print(user_data["projects"]["project1"])
      user_data["contact"]["phone"]="9212217864"
with open("user_info.json","w") as info:
      json.dump(user_data,info,indent=4)      

