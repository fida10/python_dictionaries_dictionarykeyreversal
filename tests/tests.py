import unittest
from src.ans import reverse_dictionary


class TestReverseDictionary(unittest.TestCase):
    def test_reverse_dictionary(self):
        original_dict = {'a': 1, 'b': 2, 'c': 3}
        expected = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(reverse_dictionary(original_dict), expected)

    def test_reverse_dictionary_with_duplicates(self):
        original_dict = {'a': 1, 'b': 1, 'c': 2}
        reversed_dict = reverse_dictionary(original_dict)
        self.assertEqual(len(reversed_dict), 2)
        self.assertIn(1, reversed_dict)
        self.assertIn(2, reversed_dict)

    def test_reverse_dictionary_empty(self):
        self.assertEqual(reverse_dictionary({}), {})


if __name__ == '__main__':
    unittest.main()
