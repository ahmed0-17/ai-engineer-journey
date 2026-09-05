import json


document={"name":"Ahmed","Class":9}
print(type(document))

data=json.dumps(document)  #converts dict into JSON string   dumps -> Python -> JSON

print(data)
print(type(data))


document1=json.loads(data)  #loads -> JSON  -> Python

print(document1)
print(type(document1))