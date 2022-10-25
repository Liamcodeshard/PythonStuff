class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x +self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    def draw(self, canvas):
        canvas.data[self.x:self.x+self.height, self.y:self.y + self.width] = self.color
        #^variable name ^ x position ^plus the height  ^y position then plus width
