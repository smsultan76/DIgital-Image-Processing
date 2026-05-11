import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('sm_pic.jpg', 0)
c = 255 / np.log(1 + np.max(image))
log_transformed = c * np.log(1 + image)
log_transformed = np.array(log_transformed, dtype=np.uint8)
gamma = 0.5
power_transformed = np.array(255 * (image / 255) ** gamma, dtype='uint8')
titles = ['Original Image',
          'Log Transformation',
          'Power-Law Transformation']
images = [image,
          log_transformed,
          power_transformed]
plt.figure(figsize=(12, 5))
for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
plt.tight_layout()
plt.show()