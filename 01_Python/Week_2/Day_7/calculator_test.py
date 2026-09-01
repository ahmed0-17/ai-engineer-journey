import unittest
from calculator import calculate_score
class TestCalculateScore(unittest.TestCase):

    def setUp(self):
        print("Data is ready")
        self.scores=[80,90,70]


    def tearDown(self):
     print("Test completed")

    def test_score(self):
        print("Running score test")
        result = calculate_score(self.scores)
        self.assertEqual(result, 240)

    def test_empty(self):
        print("Running score test")
        result = calculate_score([])
        self.assertEqual(result, 0)

    def test_not_equal(self):
        print("Running score test")  
        result = calculate_score([80, 90])
        self.assertNotEqual(result, 240)