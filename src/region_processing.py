from typing import Any
from skimage.measure import label, regionprops, find_contours
from skimage.morphology import remove_small_objects
import numpy as np
import pandas as pd

def extract_regions(binary_mask: np.ndarray, min_size: int = 0) -> list[dict[str, Any]]:
    """
    Extract connected regions from a binary mask using skimage.

    Args:
        binary_mask (np.ndarray): A binary image.
        min_size (int): Minimum size of objects to keep.

    Returns:
        List[Dict[str, Any]]: A list of region properties.
    """
    if min_size > 0:
        binary_mask = remove_small_objects(binary_mask, min_size=min_size)

    labeled_image = label(binary_mask, connectivity=2, background=0)
    regions = []

    for region in regionprops(labeled_image):
        region_mask = (labeled_image == region.label).astype(np.uint8) * 255
        cnts = find_contours(region_mask, level=0.5)
        cnts = np.vstack(cnts)
        cnts = pd.DataFrame(cnts[:, ::-1], columns=["x", "y"])

        regions.append({
            "label": region.label,
            "mask": region_mask,
            "area": region.area,
            "object_contour": cnts,
        })

    return sorted(regions, key=lambda r: r["area"], reverse=True)
