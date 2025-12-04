class Grandfather:
  def add(self, x, y):
    return x + y

class Grandmother(Grandfather):
  def sub(self, x, y):
    return x - y

class Father(Grandmother):
  def mul(self, x, y):
    return x * y

class Mother(Father):
  def div(self, x, y):
    return x / y

inst_obj = Mother()
print(inst_obj.add(20, 30))
print(inst_obj.sub(2, 3))
print(inst_obj.mul(2, 3))
print(inst_obj.div(4, 5))
