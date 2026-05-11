import cv2
import numpy as np
import math

original = cv2.imread('original.jpg', 0)
log_img = cv2.imread('log_output.jpg', 0)
contrast_img = cv2.imread('contrast_output.jpg', 0)
def calculate_mse_psnr(original, processed):
    mse = np.mean((original - processed) ** 2)
    if mse == 0:
        psnr = 100
    else:
        psnr = 10 * math.log10((255 * 255) / mse)
    return mse, psnr

mse_log, psnr_log = calculate_mse_psnr(original, log_img)
mse_contrast, psnr_contrast = calculate_mse_psnr(original, contrast_img)
print("Log Transformation (Lab 04):")
print("MSE:", mse_log)
print("PSNR:", psnr_log, "dB")
print("\nContrast Enhancement (Lab 05):")
print("MSE:", mse_contrast)
print("PSNR:", psnr_contrast, "dB")