# tests/test_chatbot.py
import unittest
from chatbot.main import generate_response

class TestChatbot(unittest.TestCase):

    def test_response(self):
        user_input = "Hello, how are you?"
        response, _ = generate_response(user_input)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()
