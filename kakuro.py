# Kakuro solver
import itertools

class EmptyCell:
  def draw(self):
    return "   -----  "

class DownCell:
  def __init__(self, down):
    self.down = down

  def draw(self):
    return "   {0:2d}\\--  ".format(self.down)

class AcrossCell:
  def __init__(self, across):
    self.across = across

  def draw(self):
    return "   --\\{0:2d}  ".format(self.across)

class DownAcrossCell:
  def __init__(self, down, across):
    self.down = down
    self.across = across

  def draw(self):
    return "   {0:2d}\\{1:2d}  ".format(self.down, self.across)

class ValueCell:
  def __init__(self, values):
    self.values = set(values)

  def draw_value(self, value):
    return str(value) if value in self.values else "."

  def draw(self):
    if 1 == len(self.values):
      return "     {0}    ".format(list(self.values)[0])
    else:
      return " " + "".join(map((lambda x: self.draw_value(x)), [1, 2, 3, 4, 5, 6, 7, 8, 9]))

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
  return "".join(map((lambda v: v.draw()), row)) + "\n"

def conj(coll, item):
  result = coll.copy()
  result.append(item)
  return result

def allDifferent(coll):
  return len(coll) == len(set(coll))

def permute(vs, target, soFar):
  if target >= 1:
    if len(soFar) == (len(vs) - 1):
      return [conj(soFar, target)]
    else:
      arrays = map(lambda n: permute(vs, (target - n), conj(soFar, n)), vs[len(soFar)].values)
      return list(itertools.chain.from_iterable(arrays))
  else:
    return []

def permuteAll(vs, target):
  return permute(vs, target, [])

def transpose(m):
  if 0 == len(m):
    return []
  else:
    return list(map(lambda i: list(map(lambda col: col[i], m)), range(0, len(m[0]))))

