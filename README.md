# Mosaic Generator (Modular Edition)

## Overview
This project is a **modular image mosaic generator** built for CS coursework. It transforms input images into mosaics using adjustable grid sizes, tile sizes, and color quantization, and reports similarity metrics. The user interface is built with **Gradio**, and all core logic is split across clean, maintainable modules.

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

1. **Clone** or unzip the project folder locally.  
2. Install dependencies:

```bash
pip install numpy pillow gradio scikit-image
# Optional:
pip install -r requirements.txt
Usage
Place your images in the folder specified by DATASET_PATH in config.py
(default: C:/Users/atoma/Downloads/lab1/archive/data)

Run the app:

bash
Copy code
python app.py
Open the Gradio interface in your browser.
Select or upload an image, adjust mosaic settings, and view results and metrics.

Modularity Details
All business logic (image preprocessing, tiling, mosaic building, metrics) is located inside the mosaic_generator/ module.

app.py contains only the interface and the main pipeline call; no helper functions are redefined in it.

Metric calculations use wrappers (compute_mse, compute_ssim) for readability and maintainability.

Credits
Built by Aryan Bhanushali, Northeastern University — designed for CS 5130 coursework.

css
Copy code

If you want, I can also add badges, images, usage GIFs, or a more polished intro section.
