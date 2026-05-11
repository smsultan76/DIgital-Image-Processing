from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("sm_pic.jpg")
gray_img = img.convert("L")
img_array = np.array(gray_img)
negative_img = 255 - img_array

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(gray_img, cmap='gray')
plt.title("Original Grayscale Image")

plt.subplot(1,2,2)
plt.imshow(negative_img, cmap='gray')
plt.title("Negative Image")

print("Negative Image Matrix:\n")
print(negative_img)
plt.show()