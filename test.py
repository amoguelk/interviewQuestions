import unittest
from isPalindrome import isPalindrome

class TestInterviewQuestions(unittest.TestCase):
  def testIsPalindrome(self):
    self.assertFalse(isPalindrome('supercalifragilisticexpialidocious'))
    self.assertTrue(isPalindrome('AnitaLavaLaTina'))
    self.assertTrue(isPalindrome('anitalavalatina'))


if __name__ == '__main__':
    unittest.main()