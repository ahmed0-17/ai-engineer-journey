from dataclasses import dataclass
from functools import wraps


class DocumentNotFoundError(Exception):
    pass


def logaction(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        result = function(*args, **kwargs)
        print("Called")
        return result
    return wrapper_function


def generator_log(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
        result = function(*args, **kwargs)

        for item in result:
            print("Called")
            yield item

    return wrapper_function


@dataclass
class Document:
    title: str
    content: str
    category: str


class DocumentManager:

    def __init__(self):
        self.documents = []

    @logaction
    def add_document(self, document: Document):
        self.documents.append(document)
        print("Document added Successfully")

    @logaction
    def get_document(self, title: str) -> Document:
        for document in self.documents:
            if title == document.title:
                return document
        raise DocumentNotFoundError

    @logaction
    def delete_document(self, title: str) -> None:
        for document in self.documents:
            if title == document.title:
                self.documents.remove(document)
                return

        raise DocumentNotFoundError

    @logaction
    def list_documents(self) -> None:
        if len(self.documents) > 0:
            for document in self.documents:
                print(document)
        else:
            print("There is no any document in the list")

    @logaction
    def search_document(self, title: str) -> Document:
        for document in self.documents:
            if title == document.title:
                return document

        raise DocumentNotFoundError

    @logaction
    def save_document(self) -> None:
        with open("file.txt", "w") as file:
            for document in self.documents:
                file.write("\nTitle : " + document.title + "\n")
                file.write("Content : " + document.content + "\n")
                file.write("Category : " + document.category + "\n")
                file.write("------------------------------------------------")

        print("Content Saved Successfully")

    @logaction
    def read_document(self) -> str:
        with open("file.txt", "r") as file:
            data = file.read()

        return data
    @generator_log
    def document_generator(self):
     for doc in self.documents:
      yield doc








     
doc1 = Document(
    "The AI Era",
    "The book is about building i models....",
    "Programming"
)

doc2 = Document(
    "The AI Era begins",
    "The book is about building i models....",
    "Programming"
)

manager = DocumentManager()

manager.add_document(doc1)
manager.add_document(doc2)


manager.list_documents()

manager.save_document()
print(manager.read_document())

# print(manager.search_document("The Python"))


generator = manager.document_generator()

print(next(generator))
print(next(generator))

