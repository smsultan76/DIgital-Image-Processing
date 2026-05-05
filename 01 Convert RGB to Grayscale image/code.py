import cv2
import numpy as np

# Load image
image = cv2.imread('sm_pic.jpg')

# Check if image loaded correctly
if image is None:
    print("Error: Could not load 'sm_pic.jpg'. Check the file path.")
else:
    # Convert to RGB (OpenCV loads as BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show images (using local OpenCV windows)
    cv2.imshow('Original Image', image)
    cv2.imshow('Grayscale Image', gray_image)

    # Print matrices
    print("RGB Image Matrix:\n", image_rgb)
    print("\nGrayscale Image Matrix:\n", gray_image)

    # Required for local display: wait for a key press and then close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
