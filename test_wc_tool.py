import unittest
import wc_tool


class WCTestCase(unittest.TestCase):
    def setUp(self):
        self.test_txt = "test.txt"

    def test_wc_byte_count(self):
        self.assertEqual(wc_tool.wc_byte_count(self.test_txt), 342190)  # add assertion here

    def test_wc_line_count(self):
        self.assertEqual(wc_tool.wc_line_count(self.test_txt), 7145)

    def test_wc_word_count(self):
        self.assertEqual(wc_tool.wc_word_count(self.test_txt), 58164)

    def test_wc_char_count(self):
        self.assertEqual(wc_tool.wc_char_count(self.test_txt), 339292)


if __name__ == '__main__':
    unittest.main()
