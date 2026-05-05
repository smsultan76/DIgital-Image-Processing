# Import necessary libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('sm_pic.jpg').convert('RGB')
# Convert the RGB image to Grayscale
gray_image = image.convert('L')
# Convert grayscale image to numpy array
gray_matrix = np.array(gray_image)
# Display the original and grayscale images
plt.figure(figsize=(10, 5))
# Original image
plt.subplot(1, 2, 1)
plt.title('Original RGB Image')
plt.imshow(image)
# plt.axis('off')
# Grayscale image
plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
# plt.axis('off')
plt.show()
# Display the grayscale image matrix
print("Grayscale Image Matrix:")
print(gray_matrix)