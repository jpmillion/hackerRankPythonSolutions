import unittest
from io import StringIO
from unittest.mock import patch
import mergeTheTools

class TestMergeTheTools(unittest.TestCase):

    def testMergeTheTools(self):

        with patch('sys.stdout', new = StringIO()) as string:
            mergeTheTools.merge_the_tools('aabccdeef', 3)
            self.assertEqual(string.getvalue(), "ab\ncd\nef\n")

if __name__ == '__main__':
    unittest.main()
