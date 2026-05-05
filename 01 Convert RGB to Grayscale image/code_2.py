# Import necessary libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open('sm_pic.jpg').convert('RGB')
# Convert the RGB image to Grayscale
gray_image = image.convert('L')

gray_matrix = np.array(gray_image)

plt.figure(figsize=(10, 5))
# Original image
plt.subplot(1, 2, 1)
plt.title('Original RGB Image')
plt.imshow(image)

# Grayscale image
plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.show()
# Display the grayscale image matrix
print("Grayscale Image Matrix:")
print(gray_matrix)