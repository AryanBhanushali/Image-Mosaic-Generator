# Mosaic Generator (Modular Edition)

## Overview
This project is a **modular image mosaic generator** built for CS coursework. It transforms input images into mosaics using adjustable grid sizes, tile sizes, and color quantization, and reports similarity metrics. The user interface is built with **Gradio**, and all core logic is split across individual modules.

## Features
- Fast, vectorized pipeline for mosaic construction  
- Interactive **Gradio** web interface  
- Adjustable **grid size**, **tile size**, and **color quantization** (number of buckets)  
- Reports **Mean Squared Error (MSE)** and **Structural Similarity Index (SSIM)**  
- Extensible and clean **modular design**

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
Default:

bash
Copy code
C:/Users/atoma/Downloads/lab1/archive/data
Run the app:

bash
Copy code
python app.py
Open the Gradio interface in your browser.
Upload an image, adjust mosaic settings, and view the results and metrics.

Modularity Details
All core logic (image preprocessing, tiling, mosaic building, metrics) is located inside the mosaic_generator/ module.

app.py contains only the UI and the main pipeline, with no helper functions defined directly.

Metrics use wrapper functions (compute_mse, compute_ssim) for readability and consistent usage across the project.

Credits
Built by Aryan Bhanushali, Northeastern University — designed for CS 5130 requirements.

diff
Copy code

If you want, I can add:
- a project banner,
- example output images,
- badges (Python version, license, etc.),
- or a "How It Works" section.





