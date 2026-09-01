import unittest



class RAGRetriever:

    def __init__(self, documents):
        self.documents = documents

    def get_top_document(self):
        return self.documents[0]

    def document_count(self):
        return len(self.documents)




class test_RAGRetriever(unittest.TestCase):

    def setUp(self):
         self.retriever=RAGRetriever(["Python RAG", "LLM", "FastAPI"])

    def tearDown(self):
        print("Test Completed")     


    def test_top_doc(self):
          self.assertEqual(self.retriever.documents[0],"Python RAG")


    def test_countdoc(self):
        count=self.retriever.document_count()

        self.assertEqual(count,3)      

    def test_emptydoc(self):
         self.assertRaises(IndexError,self.ret,[])   