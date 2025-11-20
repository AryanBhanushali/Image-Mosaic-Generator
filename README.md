# Mosaic Generator (Modular Edition)

## Overview
This project is a modular image mosaic generator built for CS coursework. It transforms input images into mosaics using adjustable grid sizes, tile sizes, and color quantization, and reports similarity metrics. The UI is built with Gradio, and all logic is organized into separate modules.

## Features
- Fast vectorized pipeline for mosaic generation
- Gradio web interface
- Adjustable grid size, tile size, and color quantization
- Reports MSE and SSIM similarity metrics
- Clean, extensible modular architecture

## Project Structure
`lab5/
│ app.py # Main Gradio application (entry point)
│ README.md # Project documentation
└─ mosaic_generator/
init.py
config.py # Dataset path configuration
image_processor.py # Image loading & preprocessing
mosaic_builder.py # Mosaic construction
tile_manager.py # Tile generation
metrics.py # Similarity metrics (MSE, SSIM)
utils.py # Misc utilities (example image loader)`

shell

## Installation

### Install dependencies:
`pip install numpy pillow gradio scikit-image`
`pip install -r requirements.txt` # optional

bash

## Usage

Place your images in the folder specified by `DATASET_PATH` in `config.py`.  
Default path:  
`C:/Users/atoma/Downloads/lab1/archive/data`

### Run the application:
`python app.py`

Open the Gradio interface in your browser to upload an image, tweak mosaic parameters, and view results.

## Modularity Details
- All core logic (preprocessing, tiling, mosaic building, metrics) lives inside the `mosaic_generator/` module.
- `app.py` only contains the UI + pipeline orchestration.
- Metrics use wrapper functions (`compute_mse`, `compute_ssim`) for consistency.

## Credits
Built by Aryan Bhanushali, Northeastern University — CS 5130 coursework.# Mosaic Generator (Modular Edition)

## Overview
This project is a modular image mosaic generator built for CS coursework. It transforms input images into mosaics using adjustable grid sizes, tile sizes, and color quantization, and reports similarity metrics. The UI is built with Gradio, and all logic is organized into separate modules.

## Features
- Fast vectorized pipeline for mosaic generation
- Gradio web interface
- Adjustable grid size, tile size, and color quantization
- Reports MSE and SSIM similarity metrics
- Clean, extensible modular architecture

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

## Installation

### Install dependencies:
`pip install numpy pillow gradio scikit-image`

`pip install -r requirements.txt` (optional)


## Usage

Place your images in the folder specified by `DATASET_PATH` in `config.py`.  
Default path:  
`C:/Users/atoma/Downloads/lab1/archive/data`

### Run the application:
`python app.py`

Open the Gradio interface in your browser to upload an image, tweak mosaic parameters, and view results.

## Modularity Details
- All core logic (preprocessing, tiling, mosaic building, metrics) lives inside the `mosaic_generator/` module.
- `app.py` only contains the UI + pipeline orchestration.
- Metrics use wrapper functions (`compute_mse`, `compute_ssim`) for consistency.

## Credits
Built by Aryan Bhanushali, Northeastern University, CS 5130 coursework.
