from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

# -----------------------------
# Load Original Image (PIL for contrast enhancement)
# -----------------------------
img_pil = Image.open("sm_pic.jpg").convert('RGB')
img_np = np.array(img_pil)

# Also load grayscale version for other transformations
img_gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)

# -----------------------------
# Lab 05: Contrast Enhancement
# -----------------------------
alpha = 1.5   # Contrast control
beta = 20     # Brightness control

contrast_img = np.clip(alpha * img_np + beta, 0, 255).astype(np.uint8)
contrast_gray = cv2.cvtColor(contrast_img, cv2.COLOR_RGB2GRAY)

# -----------------------------
# Lab 04: Log Transformation
# -----------------------------
c = 255 / np.log(1 + np.max(img_gray))
log_img = c * np.log(1 + img_gray)
log_img = np.array(log_img, dtype=np.uint8)

# -----------------------------
# Power-Law (Gamma) Transformation
# -----------------------------
gamma = 0.5
gamma_img = np.array(255 * (img_gray / 255) ** gamma, dtype='uint8')

# -----------------------------
# MSE & PSNR Function
# -----------------------------
def mse_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        psnr = 100
    else:
        psnr = 10 * math.log10((255 * 255) / mse)
    return mse, psnr

# -----------------------------
# Compute Metrics
# -----------------------------
mse_c, psnr_c = mse_psnr(img_gray, contrast_gray)
mse_l, psnr_l = mse_psnr(img_gray, log_img)
mse_g, psnr_g = mse_psnr(img_gray, gamma_img)

# -----------------------------
# Print Results
# -----------------------------
print("===== IMAGE QUALITY COMPARISON =====\n")

print("Contrast Enhancement:")
print("MSE :", mse_c)
print("PSNR:", psnr_c, "dB\n")

print("Log Transformation:")
print("MSE :", mse_l)
print("PSNR:", psnr_l, "dB\n")

print("Gamma Transformation:")
print("MSE :", mse_g)
print("PSNR:", psnr_g, "dB\n")

# -----------------------------
# Display Images
# -----------------------------
titles = [
    "Original Image",
    "Contrast Enhanced",
    "Log Transformation",
    "Gamma Transformation"
]

images = [img_gray, contrast_gray, log_img, gamma_img]

plt.figure(figsize=(12, 6))

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])

plt.tight_layout()
plt.show()

# -----------------------------
# Print Image Matrices (optional)
# -----------------------------
print("\nContrast Enhanced Matrix:\n", contrast_gray)
print("\nLog Transform Matrix:\n", log_img)
print("\nGamma Transform Matrix:\n", gamma_img)