📌 Overview

The Local Convexity Factor (LCF) is a geospatial metric that quantifies the convexity or concavity of a terrain based on a Digital Elevation Model (DEM). This repository provides a Python implementation to compute LCF using a sliding window approach and Pearson correlation with an idealized Gaussian surface.

🔍 Features

Processes DEM data to compute LCF at each pixel.

Uses Gaussian surface comparison to identify local convexity and concavity.

Applies Pearson correlation for quantitative measurement.

Customizable window sizes for multi-scale analysis.

Outputs LCF as a raster file for further geospatial analysis.
