from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

def plot_results(region: dict, distances: np.ndarray, contour_points: np.ndarray, max_bin_value: float) -> plt.Figure:
    """
    Creates plots for a region's mask and distance histogram.

    Args:
        region (dict): Region properties.
        distances (np.ndarray): Pairwise distances.
        contour_points (np.ndarray): Contour points.
        max_bin_value (float): Maximum bin value.

    Returns:
        plt.Figure: The created figure.
    """
    f = plt.figure(figsize=(18, 4))

    object_cnt_ax = f.add_subplot(1, 2, 1)
    object_cnt_ax.imshow(region["mask"], cmap="gray")
    object_cnt_ax.scatter(contour_points[:, 0], contour_points[:, 1], c="orange", s=0.1)
    object_cnt_ax.set_title("Object Contour")

    hist_ax = f.add_subplot(1, 2, 2)
    sns.histplot(distances, bins=100, ax=hist_ax, edgecolor="black", stat="density", kde=True)
    hist_ax.set_title(f"Distance Histogram\nMax bin value: {max_bin_value.round(2)}")

    patches = hist_ax.patches
    max_index = np.argmax([patch.get_height() for patch in patches])
    patches[max_index].set_facecolor("orange")

    plt.tight_layout(pad=2)
    plt.close(f)
    return f
