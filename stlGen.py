from numpy2stl import numpy2stl
from scipy.ndimage import gaussian_filter
from pylab import imread


A = imread("/home/jonas/MAS417_project/MAS417_project/clearsky_day.png") # read from rendered png
A = A.mean(axis=2) #grayscale projection
A = gaussian_filter(A.max() - A, 1.)

numpy2stl(A, "/home/jonas/MAS417_project/MAS417_project/test.stl", scale=0.05, solid=True, ascii=False)
