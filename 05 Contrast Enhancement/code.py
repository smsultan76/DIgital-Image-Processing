from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("sm_pic.jpg")
img_array = np.array(img)
alpha = 1.5   # Contrast control
beta = 20     # Brightness control
contrast_img = np.clip(alpha * img_array + beta, 0, 255)
contrast_img = contrast_img.astype(np.uint8)
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(1,2,2)
plt.imshow(contrast_img)
plt.title("Contrast Enhanced Image")

print("Contrast Enhanced Image Matrix:\n")
print(contrast_img)
plt.show()