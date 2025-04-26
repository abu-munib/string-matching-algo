import unittest

import string_match

class TestStringMatchingAlgorithm(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            {
                "input": "xxcakedxxxxxcakesxxx",
                "pattern": "cakes",
                "expected": [12]
            },
            {
                "input": "abcde",
                "pattern": "cde",
                "expected": [2]
            },
            {
                "input": "abcabcabcabc",
                "pattern": "abcabc",
                "expected": [0, 3, 6]
            }
        ]

    def test_naive_implementation(self):
        for i, case in enumerate(self.test_cases):
            with self.subTest(f"case {i+1}: {case['input']} -> {case['pattern']}"):
                result = string_match.naive_string_matcher(case["input"], case["pattern"])
                self.assertEqual(result, case["expected"])


    def test_kmp_preprocessing(self):
        input1 = "ababcabab"
        lps_expected1 = [0, 0, 1, 2, 0, 1, 2, 3, 4]
        lps_actual1 = string_match.kmp_preprocessing(input1)

        self.assertEqual(lps_actual1, lps_expected1)

