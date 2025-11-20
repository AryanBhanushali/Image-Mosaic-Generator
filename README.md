# Mosaic Generator (Modular Edition)

## Overview
This project is a **modular image mosaic generator** built for CS coursework. It transforms input images into mosaics using adjustable grid sizes, tile sizes, and color quantization, and reports similarity metrics. The user interface is built using **Gradio**, and all core logic is split across individual modules.

## Features
- Fast, vectorized pipeline for mosaic construction
- Interactive **Gradio** web interface
- Adjustable **grid size**, **tile size**, and **color quantization** (number of buckets)
- Reports **Mean Squared Error (MSE)** and **Structural Similarity Index (SSIM)**
- Extensible, clean **modular design**

## Project Structure
lab5/
│ app.py # Main Gradio application (entry point)
│ README.md # Project documentation
└─ mosaic_generator/
init.py
config.py # Dataset path configuration
image_processor.py # Image loading & preprocessing
mosaic_builder.py # Mosaic construction
tile_manager.py # Tile generation
metrics.py # Similarity metrics (MSE, SSIM)
utils.py # Misc utilities (example image loader)

markdown
Copy code

## Installation

1. **Clone** or download the project.
2. Install required dependencies:

```bash
pip install numpy pillow gradio scikit-image
(Optional)

bash
Copy code
pip install -r requirements.txt
Usage
Place your images in the folder specified by DATASET_PATH inside config.py.

Default:

bash
Copy code
C:/Users/atoma/Downloads/lab1/archive/data
Run the application:

bash
Copy code
python app.py
A Gradio interface will open in your browser.
Upload/select an image, adjust mosaic settings, and view results + metrics.

Modularity Details
All business logic (preprocessing, tiling, mosaic generation, metrics) is inside the mosaic_generator/ directory.

app.py only contains the UI and pipeline orchestration — no helper logic is duplicated.

Metric functions (compute_mse, compute_ssim) are wrapped for clarity and easy reuse.

Credits
Built by Aryan Bhanushali, Northeastern University — for CS 5130 coursework.
