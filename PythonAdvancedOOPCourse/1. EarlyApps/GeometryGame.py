from random import randint
import turtle

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowLeft.x < self.x < rectangle.upRight.x \
         and rectangle.lowLeft.y < self.y < rectangle.upRight.y:
            return True
        else:
            return False

    def distance_to_next_point(self, point):
        return ((point.x-self.x)**2 +
                (point.y-self.y)**2) ** 0.5


class Rectangle:

    def __init__(self, lowLeft, upRight):
        self.lowLeft = lowLeft
        self.upRight = upRight

    def area_of_Triangle(self, guess):
        if guess == (self.upRight.x - self.lowLeft.x) * (self.upRight.y - self.lowLeft.y):
            return True
        else:
            return False
class GuiRectangle(Rectangle):

    def draw(self, canvas):
        xDifference = self.upRight.x - self.lowLeft.x
        yDifference = self.upRight.y - self.lowLeft.y


        canvas.penup()
        canvas.goto(self.lowLeft.x, self.lowLeft.y)
        canvas.pendown()

        canvas.forward(xDifference)
        canvas.left(90)
        canvas.forward(yDifference)
        canvas.left(90)
        canvas.forward(xDifference)
        canvas.left(90)
        canvas.forward(yDifference)

        # turtle.done()

class GuiPoint(Point):

    def draw(self, canvas, size = 5, color = 'red'):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)
        # turtle.done()


rectangleFromRandom = GuiRectangle(Point(randint(0,200), randint(0,200)), Point(randint(200, 400), randint(200,400)))
print(f"Your Random Rectangle has the following coordinates: ({rectangleFromRandom.lowLeft.x},{rectangleFromRandom.lowLeft.y}),"
      f"({rectangleFromRandom.upRight.x},{rectangleFromRandom.upRight.y})")

user_point = GuiPoint(float(input("Guess an X coordinate that is inside the rectangle: ")),
             float(input("Guess a Y coordinate that is inside the rectangle: ")))

# print(f"Inside rectangle: {user_point.falls_in_rectangle(rectangleFromRandom)}")
#
# user_Area_Guess = int(input("Can you guess the area of the triangle? "))
# print(f"The correct area? {rectangleFromRandom.area_of_Triangle(user_Area_Guess)}")
myCanvas = turtle.Turtle()
rectangleFromRandom.draw(myCanvas)
user_point.draw(myCanvas)
turtle.done()
