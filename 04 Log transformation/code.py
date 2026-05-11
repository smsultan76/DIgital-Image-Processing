from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("sm_pic.jpg").convert("L")
img_array = np.array(img)
c = 255 / np.log(1 + np.max(img_array))
log_transformed = c * np.log(1 + img_array)
log_transformed = np.array(log_transformed, dtype=np.uint8)
gamma = 0.5
power_transformed = 255 * (img_array / 255) ** gamma

power_transformed = np.array(power_transformed, dtype=np.uint8)
plt.figure(figsize=(15,5))
plt.subplot(1,3,1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")

plt.subplot(1,3,2)
plt.imshow(log_transformed, cmap='gray')
plt.title("Log Transformation")

plt.subplot(1,3,3)
plt.imshow(power_transformed, cmap='gray')
plt.title("Power-Law Transformation")

print("Log Transformed Image Matrix:\n")
print(log_transformed)

print("\nPower-Law Transformed Image Matrix:\n")
print(power_transformed)
plt.show()