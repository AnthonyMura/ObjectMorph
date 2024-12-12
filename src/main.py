from pathlib import Path
from binary_mask import get_binary_mask
from region_processing import extract_regions
from analysis import compute_distances, analyze_distances
from visualization import plot_results


def process_region(region: dict, output_dir: Path, region_index: int) -> None:
    """
    Processes a single region and saves results.

    Args:
        region (dict): Region properties.
        output_dir (Path): Directory to save results.
        region_index (int): Region index.
    """
    contour_points = region["object_contour"].values
    distances = compute_distances(contour_points)
    _, _, _, max_bin_value = analyze_distances(distances)
    figure = plot_results(region, distances, contour_points, max_bin_value)
    figure.savefig(output_dir / f"region_{region_index}.png")


if __name__ == "__main__":
    image_path = Path("../data/example_image.tif")
    output_dir = Path("../data/results")
    output_dir.mkdir(parents=True, exist_ok=True)

    assert (
        image_path.exists() | output_dir.exists()
    ), "Image or output directory does not exist"

    binary_mask = get_binary_mask(image_path)
    regions = extract_regions(binary_mask, min_size=0)

    for region_index, region in enumerate(regions[:6]):
        process_region(region, output_dir, region_index)
