# documents = []
#        ↓
# 3 documents append karo
#        ↓
# JSON file mein save karo
#        ↓
# JSON file read karo
#        ↓
# 2nd document update karo
#        ↓
# 1 document delete karo
#        ↓
# updated data JSON mein save karo


import json

documents=[]

documents.append({
                  "name":"Ahmed Ali Malik",
                  "contact":
                  {
                   "phone":"1212324334",
                   "email":"ahmed543@gmail.com"
                   },
                  "education":
                  {
                      "university":"UOS",
                   "college":"FG Degree College"
                   }
                   })
documents.append({
                  "name":"Abid Ali",
                  "contact":
                  {
                   "phone":"434354233",
                   "email":"abid543@gmail.com"
                   },
                  "education":
                  {
                      "university":"UOS",
                   "college":"Superior Degree College"
                   }
                   })
documents.append({
                  "name":"Ali",
                  "contact":
                  {
                   "phone":"1212342334",
                   "email":"ali443@gmail.com"
                   },
                  "education":
                  {
                      "university":"UOS",
                   "college":"FG Degree College"
                   }
                   })


with open("user.json","w") as users:
    json.dump(documents,users,indent=4)
with open("user.json","r") as users:
    data=json.load(users)
    data[1]={
                  "name":"Abid Ali Raza",
                  "contact":
                  {
                   "phone":"43435423332",
                   "email":"abid5213@gmail.com"
                   },
                  "education":
                  {
                      "university":"UOS",
                   "college":"Superior Degree College Hyd"
                   }
                   }
    data.pop(2)

with open("user.json","w") as users:
      json.dump(data,users,indent=4)
      
