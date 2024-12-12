from pathlib import Path
import numpy as np
import cv2

def get_binary_mask(image_path: Path) -> np.ndarray:
    """
    Converts an image to a binary mask using Otsu's thresholding.

    Args:
        image_path (Path): Path to the image file.

    Returns:
        np.ndarray: Binary mask.
    """
    grey_image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)
    binary = cv2.threshold(grey_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return binary
