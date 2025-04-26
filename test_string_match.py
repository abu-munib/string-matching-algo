import unittest

import string_match

class TestStringMatchingAlgorithm(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            {
                "input": "xxcakedxxxxxcakesxxx",
                "pattern": "cakes",
                "expected": True
            },
            {
                "input": "abcde",
                "pattern": "cde",
                "expected": True
            }
        ]

    def test_naive_implementation(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"case {i+1}: {case['input']} -> {case['pattern']}"):
                result = string_match.naive_string_matcher(case["input"], case["pattern"])
                self.assertEqual(result, case["expected"])


