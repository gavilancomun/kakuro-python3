import unittest

from itertools import *
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

  def test_transpose(self):
    ints = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
    tr = transpose(ints)
    print(ints)
    print(tr)
    self.assertEqual(len(ints), len(tr[0]))
    self.assertEqual(len(ints[0]), len(tr))

  def test_takewhile(self):
    result = list(takewhile(lambda n: n < 4, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(result)
    self.assertEqual(4, len(result))

  def test_concat(self):
    a = [1, 2, 3]
    b = [4, 5, 6, 1, 2, 3]
    result = concatLists(a, b)
    print(result)
    self.assertEqual(9, len(result))

  def test_drop(self):
    a = [1, 2, 3, 4, 5, 6]
    result = a[4:]
    print(result)
    self.assertEqual(2, len(result))

  def test_take(self):
    a = [1, 2, 3, 4, 5, 6]
    result = a[:4]
    print(result)
    self.assertEqual(4, len(result))

  def test_partby(self):
    data = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9]
    result = partitionBy(lambda n: 0 == (n % 2), data)
    print(result)
    self.assertEqual(9, len(result))

  def test_partall(self):
    data = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 8, 9]
    result = partitionAll(5, 3, data)
    print(result)
    self.assertEqual(5, len(result))

  def test_last(self):
    data = [1, 2, 3, 4]
    self.assertEqual(4, last(data))

  def test_isposs(self):
    vc = v(1, 2, 3)
    result = isPossible(vc, 2)
    self.assertTrue(result)
    result = isPossible(vc, 4)
    self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()

