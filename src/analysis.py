import numpy as np


def compute_distances(contour_points: np.ndarray) -> np.ndarray:
    """
    Computes pairwise distances between points in a contour.

    Args:
        contour_points (np.ndarray): Array of contour points.

    Returns:
        np.ndarray: Pairwise distances.
    """
    squared_distances = np.square(
        contour_points[:, np.newaxis, :] - contour_points[np.newaxis, :, :]
    )
    squared_distances = np.sum(squared_distances, axis=-1)
    distances = np.sqrt(squared_distances)
    distances = np.triu(distances).reshape(-1)
    return distances[distances != 0]


def analyze_distances(distances: np.ndarray, bins: int = 100):
    """
    Analyzes distance data to compute a histogram and max bin.

    Args:
        distances (np.ndarray): Pairwise distances.
        bins (int): Number of histogram bins.

    Returns:
        Tuple: Histogram, bin edges, max index, and max bin value.
    """
    hist, bin_edges = np.histogram(distances, bins=bins)
    max_index = np.argmax(hist)
    max_bin_value = bin_edges[max_index]
    return hist, bin_edges, max_index, max_bin_value
