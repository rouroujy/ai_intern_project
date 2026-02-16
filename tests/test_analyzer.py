import unittest
from app.analyzer import analyze_text

class TestAnalyzer(unittest.TestCase):

    def test_basic_analyze(self):
        result = analyze_text("data/sample.txt")
        self.assertTrue(result['lines']>0)
        self.assertTrue(result['words']>0)


if __name__ =="__main__":
    unittest.main()