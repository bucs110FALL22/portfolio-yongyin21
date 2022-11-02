#why classes?
#class vs dictionary 
#no difference 
#classes encapsulate behavior
num = 5 
t = range(10)
mystr = "This is a string with a " +  str(num) +  "and" +  str(t)
print(mystr)
#F string allow inseting a variable into a string sorround variables with '' and use f at beginning of string

#Magic Methods
#any methods sorrounded by underscores 
#used by python
class Num:
  def __init__(self, x =0):
    self.num = x

  def __str__(self):
    return str(self.num)
#anytime I want to stringify serialize string : __str__
#don't print in your __str__ method 
n = Num()
print(n)
print(id(n))

class Graph:
  def __init__(self, title="My Graph"):
    self.points = []
    self.title = title

  def add_point(self,p):
    self.points.append(p)

  def __str__(self):
    point_str = ""
    for p in self.points:
      point_str = f ""
    return self.title
  def main():
    g = Graph()
    print(g)

main()