import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)

output = img.copy()  # The original image is read-only!
output[:, :, :2] = 0
mpimg.imsave("blue.jpg", output)
