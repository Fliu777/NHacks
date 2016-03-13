import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('map2_small.png')
lum_img = img[:,:,0]
imgplot = plt.imshow(lum_img)
plt.colorbar()
plt.show()