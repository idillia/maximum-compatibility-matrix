import unittest

def isOdd(n):
  return n % 2 == 1

class IsOddTests(unittest.TestCase):

  def testOne(self):
    self.failUnless(isOdd(1))

  def testTwo(self):
    self.failIf(isOdd(2))

def main():
  unittest.main()

if __name__ == '__main__':
  main()
