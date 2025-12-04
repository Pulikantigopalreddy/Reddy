class Grandfather:
  def add(x, y):
    return x + y

class Grandmother(Grandfather):
  def sub(x, y):
    return x - y

class Father(Grandmother):
  def mul(x, y):
    return x * y

class Mother(Father):
  def div(x, y):
    return x / y

inst_obj = Mother
print(inst_obj.add(20, 30))
print(inst_obj.sub(2, 3))
print(inst_obj.mul(2, 3))
print(inst_obj.div(4, 5))
