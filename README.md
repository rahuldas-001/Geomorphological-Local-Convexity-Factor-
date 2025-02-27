📌 Overview

The Local Convexity Factor (LCF) is a geospatial metric that quantifies the convexity or concavity of a terrain based on a Digital Elevation Model (DEM) based on (Liu et.al 2025,https://doi.org/10.1016/j.gsf.2024.101960). This repository provides a Python implementation to compute LCF using a sliding window approach and Pearson correlation with an idealized Gaussian surface.

🔍 Features

Processes DEM data to compute LCF at each pixel.

Uses Gaussian surface comparison to identify local convexity and concavity.

Applies Pearson correlation for quantitative measurement.

Customizable window sizes for multi-scale analysis.

Outputs LCF as a raster file for further geospatial analysis.


![image](https://github.com/user-attachments/assets/e31c905a-8fa8-4762-a310-e5d504f25bbb)  ![image](https://github.com/user-attachments/assets/67e7383f-becb-44ca-a336-a1f2ef216e97)




📊 Applications

LCF is particularly useful in geomorphology and hazard assessment, including:

Landslide Susceptibility Analysis: Identifies convex landforms prone to failure.

Flood Susceptibility Mapping: Highlights depressions and low-lying flood-prone regions.

Terrain Classification: Distinguishes between valleys, ridges, and plateaus.

Hydrological & Erosion Studies: Helps in modeling surface runoff patterns.


