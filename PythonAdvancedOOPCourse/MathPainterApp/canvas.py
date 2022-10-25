import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # initialise a 3d numpy array with 0's
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        # change the 0's to new color
        self.data[:] = self.color


    def Make(self, image_path):
        # convert array into image file
        img = Image.fromarray(self.data, "RGB")
        img.save(image_path)
