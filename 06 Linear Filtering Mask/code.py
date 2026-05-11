import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('sm_pic.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
smooth_3x3 = cv2.blur(image, (3, 3))
smooth_5x5 = cv2.blur(image, (5, 5))
smooth_7x7 = cv2.blur(image, (7, 7))
smooth_9x9 = cv2.blur(image, (9, 9))
titles = ['Original Image', '3x3 Filter', '5x5 Filter', '7x7 Filter', '9x9 Filter']
images = [image, smooth_3x3, smooth_5x5, smooth_7x7, smooth_9x9]
plt.figure(figsize=(15, 8))
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])

plt.tight_layout()
plt.show()