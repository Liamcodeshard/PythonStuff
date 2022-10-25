import random

from OOPLearning.RaspberryPi.Shapes import Paper, Rectangle, Oval, Triangle



# First we need a piece of paper
paper = Paper()

#Design Tangle
rect1 = Rectangle()
rect1.set_color("white")
rect1.set_height(200)
rect1.set_width(300)

door = Rectangle()
door.set_color("red")
door.set_height(60)
door.set_width(40)
door.set_x(410)
door.set_y(415)

window1 = Rectangle()
window1.set_color("teal")
window1.set_height(60)
window1.set_width(60)
window1.set_x(320)
window1.set_y(400)

window2 = Rectangle()
window2.set_color("teal")
window2.set_height(60)
window2.set_width(60)
window2.set_x(480)
window2.set_y(400)

window3 = Rectangle()
window3.set_color("teal")
window3.set_height(60)
window3.set_width(60)
window3.set_x(320)
window3.set_y(310)

window4 = Rectangle()
window4.set_color("teal")
window4.set_height(60)
window4.set_width(60)
window4.set_x(480)
window4.set_y(310)

chimney = Rectangle()
chimney.set_color("brown")
chimney.set_height(60)
chimney.set_width(30)
chimney.set_x(500)
chimney.set_y(200)

roof = Triangle(275,275, 575, 275, 425, 200)
roof.set_color("orange")

# sun = Oval()
# sun.randomize()
# sun.set_color("yellow")

sun2 = Oval(width=50, height=100, x=None, y=None, color="orange")
sun2.set_x(random.randint(100,300))
sun2.set_y(random.randint(100,300))
#Draw Shapes

# rect1.draw()
# door.draw()
# window1.draw()
# window2.draw()
# window3.draw()
# window4.draw()
# chimney.draw()
# roof.draw()

def drawHouse():
    rect1.draw()
    door.draw()
    window1.draw()
    window2.draw()
    window3.draw()
    window4.draw()
    chimney.draw()
    roof.draw()
    sun.draw()
    sun2.draw()


# made a function to draw a house
drawHouse()


#Show Drawing
paper.display()
