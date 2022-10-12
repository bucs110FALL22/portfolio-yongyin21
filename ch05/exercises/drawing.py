import turtle
def drawEQShape():
  steve = turtle.Turtle()
  steve.shape = ("turtle")
  steve.color = ("green")
  sidelength = int(input("Length of sides?"))
  number_of_sides = int(input("Number of sides?"))
  angle = 360 /number_of_sides
  for i in [angle]*number_of_sides:
    steve.forward(sidelength)
    steve.left(i) 
drawEQShape()
turtle.done()

  

  