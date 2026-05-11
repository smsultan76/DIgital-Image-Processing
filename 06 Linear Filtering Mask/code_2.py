import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sm_pic.jpg', 0)
mask_sizes = [3, 5, 7, 9]
images = [img]
titles = ['Original']

for size in mask_sizes:
    smoothed = cv2.blur(img, (size, size))
    images.append(smoothed)
    titles.append(f'Smoothing {size}x{size}')

plt.figure(figsize=(15, 10))
for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])

plt.tight_layout()
plt.show()