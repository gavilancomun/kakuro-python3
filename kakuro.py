# Kakuro solver
from itertools import *

class EmptyCell:
  def draw(self):
    return "   -----  "

  def __eq__(self, other):
    return isinstance(other, self.__class__)

class DownCell:
  def __init__(self, down):
    self.down = down

  def draw(self):
    return "   {0:2d}\\--  ".format(self.down)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and (self.down == other.down))

class AcrossCell:
  def __init__(self, across):
    self.across = across

  def draw(self):
    return "   --\\{0:2d}  ".format(self.across)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and (self.across == other.across))

class DownAcrossCell:
  def __init__(self, down, across):
    self.down = down
    self.across = across

  def draw(self):
    return "   {0:2d}\\{1:2d}  ".format(self.down, self.across)

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and (self.across == other.across) and (self.down == other.down))

class ValueCell:
  def __init__(self, values):
    self.values = set(values)

  def draw_value(self, value):
    return str(value) if value in self.values else "."

  def draw(self):
    if 1 == len(self.values):
      return "     {0}    ".format(list(self.values)[0])
    else:
      return " " + "".join(map(lambda x: self.draw_value(x), [1, 2, 3, 4, 5, 6, 7, 8, 9]))

  def __eq__(self, other):
    return (isinstance(other, self.__class__) and (self.values == other.values))

def e():
  return EmptyCell()

def a(across):
  return AcrossCell(across)

def d(down):
  return DownCell(down)

def da(down, across):
  return DownAcrossCell(down, across)

def v(*args):
  if 0 == len(args):
    return ValueCell([1, 2, 3, 4, 5, 6, 7, 8, 9])
  else:
    return ValueCell(args)

def drawRow(row):
  return "".join(map(lambda v: v.draw(), row)) + "\n"

def conj(coll, item):
  result = coll.copy()
  result.append(item)
  return result

def allDifferent(coll):
  return len(coll) == len(set(coll))

def concatLists(coll1, coll2):
  return list(chain.from_iterable([coll1, coll2]))

def permute(vs, target, soFar):
  if target >= 1:
    if len(soFar) == (len(vs) - 1):
      return [conj(soFar, target)]
    else:
      arrays = map(lambda n: permute(vs, (target - n), conj(soFar, n)), vs[len(soFar)].values)
      return list(chain.from_iterable(arrays))
  else:
    return []

def permuteAll(vs, target):
  return permute(vs, target, [])

def transpose(m):
  if 0 == len(m):
    return []
  else:
    return list(map(lambda i: list(map(lambda col: col[i], m)), range(0, len(m[0]))))

def partitionBy(f, coll):
  if 0 == len(coll):
    return []
  else:
    head = coll[0]
    fx = f(head)
    group = list(takewhile(lambda y: fx == f(y), coll))
    return concatLists([group], partitionBy(f, coll[len(group):]))

def partitionAll(n, step, coll):
  if 0 == len(coll):
    return []
  else:
    return concatLists([coll[:n]], partitionAll(n, step, coll[step:]))

def partitionN (n, coll):
  return partitionAll(n, n, coll)

def last(coll):
  return coll[len(coll) - 1]

def isPossible(v, n):
  return any(map(lambda item: item == n, v.values))

def solveStep(cells, total):
  finalIndex = len(cells) - 1
  perms = permuteAll(cells, total)
  perms2 = list(filter(lambda v: isPossible(last(cells), v[finalIndex]), perms))
  perms3 = list(filter(lambda v: allDifferent(v), perms2))
  perms4 = transpose(perms3)
  return list(map(lambda coll: v(*coll), perms4))

# returns (non-vals, vals)*
def gatherValues(line):
  return partitionBy(lambda v: isinstance(v, ValueCell), line)

def pairTargetsWithValues(line):
  return partitionN(2, gatherValues(line))


