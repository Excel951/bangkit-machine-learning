from rearrange import rearrange_name

print(rearrange_name('Lovelace, Ada'))

# Writing unittest in python
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = 'Lovelace, Ada'
        expected = 'Ada Lovelace'
        self.assertEqual(rearrange_name(testcase), expected)
        
    # def test_wrong_name(self):
    #     testcase = 'Lovelace Ada'
    #     expected = testcase
    #     self.assertEqual(rearrange_name(testcase), expected)
        
    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_double_name(self):
        testcase = 'Hopper, Grace M.'
        expected = 'Grace M. Hopper'
        self.assertEqual(rearrange_name(testcase), expected)
        
    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)
        
unittest.main()