from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("sm_pic.jpg")
img_array = np.array(img)
brightness = 50
bright_img = np.clip(img_array + brightness, 0, 255)
bright_img = bright_img.astype(np.uint8)

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")
plt.subplot(1,2,2)
plt.imshow(bright_img)
plt.title("Brightness Enhanced Image")

print("Brightness Enhanced Image Matrix:\n")
print(bright_img)
plt.show()