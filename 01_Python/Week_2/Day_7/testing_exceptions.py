import unittest

def get_top_document(documents):
    return documents[0]




class test_method(unittest.TestCase):
 def test_empty_documents(self):
   self.assertRaises(IndexError,get_top_document,[])

 def test_valid_documents(self):
    result = get_top_document(["Python", "RAG", "LLM"])
    self.assertEqual(result, "Python")     