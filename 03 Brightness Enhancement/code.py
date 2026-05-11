import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sm_pic.jpg')
brightness = 50
bright_img = cv2.convertScaleAbs(img, beta=brightness)
titles = ['Original Image', 'Brightness Enhanced Image']
images = [img, bright_img]
plt.figure(figsize=(10, 5))
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    
plt.tight_layout()
plt.show()