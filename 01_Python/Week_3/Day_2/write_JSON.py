import json


document=[
        {
          "name":"Ahmed",
          "age":22,
          "skills":["Python","JS","FastAPI"],
          "university":"University of Sindh"
          },
          {
          "name":"Ali",
          "age":21,
          "skills":["Python","CPP","React"],
          "university":"University of Sindh"
          },
          ]

with open("document.json","r") as file:
    # json.dump(document,file,indent=4)
    data=json.load(file)
    data[0]["age"]=27
    data.append({
        "name":"Bilal",
         "age":22,
         "skills":["Java","Project Management","AI"],
         "university":"University of Sindh"
    })
    data.pop(2)

with open("document.json","w") as file:
    json.dump(data,file,indent=4)


    