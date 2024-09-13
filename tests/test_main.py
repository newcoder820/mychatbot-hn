import unittest
from chatbot.main import main

class TestChatbot(unittest.TestCase):

    def test_main(self):
        # Simple test to check if main function runs
        try:
            main()
            self.assertTrue(True)
        except:
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()