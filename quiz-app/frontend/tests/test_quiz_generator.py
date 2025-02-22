import unittest
from app.quiz_generator import generate_quiz, extract_key_info

class TestQuizGenerator(unittest.TestCase):

    def test_extract_key_info(self):
        text = "Albert Einstein was a German-born theoretical physicist."
        key_info = extract_key_info(text)
        self.assertIn("Albert Einstein", key_info)
        self.assertIn("German", key_info)

    def test_generate_quiz(self):
        text = "Python is a high-level programming language."
        num_questions = 3
        quiz = generate_quiz(text, num_questions)
        self.assertIsInstance(quiz, str)
        self.assertIn("Q:", quiz)
        self.assertIn("A)", quiz)
        self.assertIn("Correct Answer:", quiz)

if __name__ == '__main__':
    unittest.main()
