# Image Region Analysis and Visualization

This project processes binary images to extract regions, compute distances between object contours, analyze histograms, and visualize the results. It is designed for scientific and analytical purposes, leveraging tools like OpenCV, scikit-image, and Matplotlib.

---

## Features

- Convert grayscale images to binary masks using Otsu's thresholding.
- Extract and label regions from binary masks.
- Compute pairwise distances between contour points of detected regions.
- Analyze histograms of distances and identify significant bins.
- Visualize region masks and distance histograms.
- Modular and reusable code for flexible workflows.

---

## Project Structure

.
├── src/
│ ├── init.py # Marks the folder as a Python package
│ ├── binary_mask.py # Handles binary mask creation
│ ├── region_processing.py # Extracts and processes image regions
│ ├── analysis.py # Performs distance computation and analysis
│ ├── visualization.py # Visualizes results
│ └── main.py # Entry point for the project
├── data/
│ ├── example_image.tif # Example input image
│ ├── results/ # Output directory for visualizations
├── requirements.txt # Dependencies
└── README.md # Project overview and usage

---

## Installation

### Prerequisites

Ensure you have Python 3.8 or higher installed.

### Install Dependencies

Create a virtual environment and install required packages:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
