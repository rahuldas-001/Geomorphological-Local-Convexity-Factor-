📌 Overview

The Local Convexity Factor (LCF) is a geospatial metric that quantifies the convexity or concavity of a terrain based on a Digital Elevation Model (DEM) based on (Liu et.al 2025,https://doi.org/10.1016/j.gsf.2024.101960). This repository provides a Python implementation to compute LCF using a sliding window approach and Pearson correlation with an idealized Gaussian surface.

🔍 Features

Processes DEM data to compute LCF at each pixel.

1. Uses Gaussian surface comparison to identify local convexity and concavity.

2. Applies Pearson correlation for quantitative measurement.

3. Customizable window sizes for multi-scale analysis.

4. Outputs LCF as a raster file for further geospatial analysis.

![image](https://github.com/user-attachments/assets/bc0a8b53-fd2b-4b0a-8d3f-d5a58e518c96)![image](https://github.com/user-attachments/assets/67e7383f-becb-44ca-a336-a1f2ef216e97)




📊 Applications

LCF is particularly useful in geomorphology and hazard assessment, including:

1. Landslide Susceptibility Analysis: Identifies convex landforms prone to failure.

2. Flood Susceptibility Mapping: Highlights depressions and low-lying flood-prone regions.

3. Terrain Classification: Distinguishes between valleys, ridges, and plateaus.

4. Hydrological & Erosion Studies: Helps in modeling surface runoff patterns.


