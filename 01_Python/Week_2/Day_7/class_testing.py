import unittest

class Document:

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_preview(self):
        return self.content[:20]



class TestDocumnent(unittest.TestCase):

    def setUp(self):
     self.model=Document("The Kite Runner","The story is starting about 18 years ago......")

    def test_title(self):
       self.assertEqual(self.model.title,"The Kite Runner")

    def test_content(self):
       self.assertEqual(self.model.content,"The story is starting about 18 years ago......")

    def test_get_preview(self):
       result=self.model.get_preview()   
       self.assertEqual(result,self.model.content[:20])
        
    