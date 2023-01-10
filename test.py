import unittest
from isPalindrome import isPalindrome
from findRepeatedNumber import findRepeatedNumber

class TestInterviewQuestions(unittest.TestCase):
  def testIsPalindrome(self):
    self.assertFalse(isPalindrome('supercalifragilisticexpialidocious'))
    self.assertTrue(isPalindrome('AnitaLavaLaTina'))
    self.assertTrue(isPalindrome('anitalavalatina'))
  
  def testFindRepeatedNumber(self):
    self.assertEqual(findRepeatedNumber([3,2,3,1,4]), 3)
    self.assertEqual(findRepeatedNumber([9, 11, 5, 1, 12, 13, 8, 10, 7, 14, 2, 6, 15, 16, 17, 18, 19, 4, 3, 10]), 10)


if __name__ == '__main__':
    unittest.main()