import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)

averages = img.mean(axis=2)  # Take the average of each R, G, and B
mpimg.imsave("bad-gray.jpg", averages, cmap="gray")
