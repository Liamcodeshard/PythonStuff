from OOPLearning.PythonAdvancedOOPCourse.MathPainterApp.canvas import Canvas
from OOPLearning.PythonAdvancedOOPCourse.MathPainterApp.shapes import Square, Rectangle

colour_library = {"white" : (255,255,255), "black": (0,0,0), "blue":(0,0,255), "red" : (255, 0, 0), "green": (0,250,0) }

canvas_width = int(input("How wide would you like the canvas? \n >> "))
canvas_height = int(input("How high would you like the canvas? \n >> "))
canvas_colour = input("What colour would you like the canvas? Write 'black' or 'white':  \n >> ")
canvas = Canvas(width=canvas_width, height=canvas_height, color=colour_library[canvas_colour])
shape_choice = ""

while True:
    # Ask what user wants to draw
    shape_choice = input(
        "What would you like to draw? Type: 'square', 'rectangle' or any other input to quit. \n >> ")
    # get rectangle data
    if shape_choice == 'rectangle':


        rectangle_x = int(input("Please choose the x position for the top left corner of the rectangle:  \n >> "))
        rectangle_y = int(input("Please choose the y position for the top left corner of the rectangle:  \n >> "))
        rectangle_height = int(input("Please choose the height of the rectangle:  \n >> "))
        rectangle_width = int(input("Please choose the width of the rectangle:  \n >> "))
        rectangle_color_red = 25.5*int(input("Please choose the intensity of red for the square (between 1-10)  \n >> "))
        rectangle_color_green = 25.5*int(input("Please choose the intensity of green for the square (between 1-10)  \n >> "))
        rectangle_color_blue = 25.5*int(input("Please choose the intensity of blue for the square (between 1-10)  \n >> "))
        #shape_choice = input("What would you like to draw? Type: 'square', 'rectangle' or any other input to quit. \n >> ")

        rectangle1 = Rectangle(x=rectangle_x, y=rectangle_y, height=rectangle_height, width=rectangle_width, color=(rectangle_color_red,rectangle_color_green, rectangle_color_blue))
        rectangle1.draw(canvas)


    if shape_choice == 'square':
        square_x = int(input("Please choose the x position for the top left corner of the square:  \n >> "))
        square_y = int(input("Please choose the y position for the top left corner of the square:  \n >> "))
        square_side = int(input("Please choose the height of the sides of the square:  \n >> "))
        square_color_red = 25.5*int(input("Please choose the intensity of red for the square (between 1-10)  \n >> "))
        square_color_green = 25.5*int(input("Please choose the intensity of green for the square (between 1-10)  \n >> "))
        square_color_blue = 25.5*int(input("Please choose the intensity of blue for the square (between 1-10)  \n >> "))
        #shape_choice = input("What would you like to draw? Type: 'square', 'rectangle' or any other input to quit. \n >> ")

        square1 = Square(x=square_x, y=square_y, side=square_side, color=(square_color_red,square_color_green, square_color_blue))
        square1.draw(canvas)

    if shape_choice == 'quit':
        break

canvas.Make('files/canvas.png')