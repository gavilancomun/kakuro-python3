import unittest
from kakuro import *

class TestStringMethods(unittest.TestCase):

  def test_upper(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_isupper(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_drawrow(self):
    line = [da(3, 4), v(), v(1, 2), d(4), e(), a(5), v(4), v(1)]
    result = drawRow(line)
    print("drawrow")
    print(result)
    self.assertEqual("    3\\ 4   123456789 12.......    4\\--     -----     --\\ 5       4         1    \n", result)

  def test_permute(self):
    vs = [v(), v(), v()]
    results = permuteAll(vs, 6)
    print(results)
    self.assertEqual(10, len(results))
    diff = list(filter((lambda p: allDifferent(p)), results))
    self.assertEqual(6, len(diff))


if __name__ == '__main__':
    unittest.main()

