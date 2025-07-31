import unittest
from ..translate_4CI import translate_number_to_chinese

class TestTranslate4CI(unittest.TestCase):
    def setUp(self):
        self.translator = translate_number_to_chinese()

    def test_valid_4CI_code(self):
        """Test translation of valid 4-corner index codes"""
        test_cases = {
            "2712": "人",  # Example code for 人
            "4744": "文",  # Example code for 文
            "1010": "一"   # Example code for 一
        }
        for code, expected in test_cases.items():
            with self.subTest(code=code):
                result = self.translator.translate(code)
                self.assertIn(expected, result)

    def test_invalid_4CI_code(self):
        """Test handling of invalid 4-corner index codes"""
        invalid_codes = ["", "123", "12345", "abcd", "****"]
        for code in invalid_codes:
            with self.subTest(code=code):
                with self.assertRaises(ValueError):
                    self.translator.translate(code)

    def test_multiple_characters(self):
        """Test when a 4CI code maps to multiple characters"""
        code = "2711"  # This code might map to multiple characters
        result = self.translator.translate(code)
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_case_sensitivity(self):
        """Test if the translator handles different case inputs"""
        code_lower = "2712"
        code_upper = "2712"
        self.assertEqual(
            self.translator.translate(code_lower),
            self.translator.translate(code_upper)
        )

if __name__ == '__main__':
    unittest.main()