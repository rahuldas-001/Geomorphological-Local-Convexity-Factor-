# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:59:21 2025

@author: DELL
"""

import numpy as np
import rasterio
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from tqdm import tqdm
import os

os.chdir("D:/AIRBMP/Paper related work/LCF")

def normalize(arr):
    """Min-max normalization for local DEM windows."""
    min_val = np.min(arr)
    max_val = np.max(arr)
    return (arr - min_val) / (max_val - min_val) if max_val > min_val else arr

def create_gaussian_surface(size):
    """Generate a 2D Gaussian surface with an adaptive sigma."""
    sigma = size / 6  # Adaptive standard deviation
    x = np.linspace(-size//2, size//2, size)
    y = np.linspace(-size//2, size//2, size)
    X, Y = np.meshgrid(x, y)
    gaussian_surface = np.exp(-(X**2 + Y**2) / (2 * sigma**2))
    return normalize(gaussian_surface)  # Normalize to match DEM range

def compute_lcf(dem, min_window=2, max_window=50):
    """Compute Local Convexity Factor (LCF) with performance improvements."""
    rows, cols = dem.shape
    lcf = np.full((rows, cols), np.nan)  # Initialize with NaNs

    for i in tqdm(range(rows), desc="Processing LCF Rows"):
        for j in range(cols):
            max_corr = -1  # Start with low correlation
            for window_size in range(min_window, max_window+1, 2):
                half_w = window_size // 2

                # Ensure window is within bounds
                if (i - half_w >= 0 and i + half_w < rows) and (j - half_w >= 0 and j + half_w < cols):
                    local_window = dem[i-half_w:i+half_w+1, j-half_w:j+half_w+1]
                    local_window = normalize(local_window)  # Normalize per window

                    gaussian_window = create_gaussian_surface(local_window.shape[0])

                    # Compute Pearson correlation
                    corr, _ = pearsonr(local_window.flatten(), gaussian_window.flatten())
                    max_corr = max(max_corr, corr)

            lcf[i, j] = max_corr  # Assign max correlation as LCF

    return lcf

# Load DEM and Compute LCF
with rasterio.open("fill.tif") as dataset:
    dem_data = dataset.read(1).astype(np.float32)

    lcf_result = compute_lcf(dem_data)

# Plot LCF Before Saving
plt.figure(figsize=(10, 8))
plt.imshow(lcf_result, cmap="viridis", interpolation="nearest")
plt.colorbar(label="Local Convexity Factor (LCF)")
plt.title("LCF Computed from DEM")
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.show()

# Save LCF Output
save_choice = input("Save LCF raster? (yes/no): ")
if save_choice.lower() == "yes":
    with rasterio.open("fill.tif") as dataset:
        meta = dataset.meta.copy()
    meta.update(dtype=rasterio.float32)

    with rasterio.open("lcf_output.tif", "w", **meta) as dst:
        dst.write(lcf_result, 1)

    print("LCF calculation complete. Saved as 'lcf_output.tif'.")
else:
    print("LCF was not saved.")