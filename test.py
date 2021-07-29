import unittest

class BoolTest(unittest.TestCase):
    def test_isupper(self):
        self.assertFalse('foo'.isupper())

if __name__ == '__main__':
    unittest.main()