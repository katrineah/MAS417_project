from numpy2stl import numpy2stl
from scipy.ndimage import gaussian_filter
from pylab import imread
from text2png import text2png

class stlGen:

    def __init__(self):
        pass
    def generate_png(self, text):
        self.text = text
        text = f"{self.text}"
        text2png(text,"/home/jonas/MAS417_project/MAS417_project/textPNG", fontsize = 40)
        A = imread("/home/jonas/MAS417_project/MAS417_project/textPNG.png",2) # read from rendered png
        A = A.mean(axis=2) #grayscale projection
        A = gaussian_filter(A.max()-A, 0.6)
        numpy2stl(A,"/home/jonas/MAS417_project/MAS417_project/weatherData.stl", scale=0.1, solid=True, ascii=False)

