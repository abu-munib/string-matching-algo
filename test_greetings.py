import unittest

import main

class TestGreetings(unittest.TestCase):

    def test_greetings(self):
        self.assertEqual(main.greetings(), "Hello!")

if __name__ == '__main__':
    unittest.main()

