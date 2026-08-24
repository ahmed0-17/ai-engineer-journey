from dataclasses import dataclass,field

@dataclass
class Document:
    title:str
    content:str
    tags:list=field(default_factory=list)
    metadata:dict=field(default_factory=dict)
    



doc1=Document("Saas Project doc","...")
doc2=Document("Office files","...")
doc1.metadata["page"]=33
doc1.tags.append("<html>")

print(doc1)
print(doc2)










