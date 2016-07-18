# Kakuro solver

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
