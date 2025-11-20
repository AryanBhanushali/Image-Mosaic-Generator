import numpy as np
from PIL import Image
import gradio as gr
import time
from skimage.metrics import mean_squared_error, structural_similarity as ssim
import glob
import os
from mosaic_generator.config import DATASET_PATH
from mosaic_generator.image_processor import preprocess_image, image_to_grid, classify_cells
from mosaic_generator.tile_manager import build_tile_set
from mosaic_generator.mosaic_builder import reconstruct_image_vectorized
from mosaic_generator.utils import get_example_images
from mosaic_generator.metrics import compute_mse, compute_ssim

# Main processing function for Gradio
def mosaicify_vectorized(img, grid_size, tile_size, n_colors):
    t0 = time.time()
    # Step 1: Preprocess and crop image to grid multiple
    img = preprocess_image(img, grid_size)
    # Step 2: Divide to grid, average, quantize
    cells = image_to_grid(img, grid_size)
    classified = classify_cells(cells, n_colors)
    # Step 3: Build tile set (colored tiles only)
    tiles, colors = build_tile_set(tile_size, n_colors)
    # Step 4: Mosaic image
    mosaic = reconstruct_image_vectorized(classified, tiles, colors, tile_size)
    # Segmentation as an upscaled grid of average colors (for interactive visualization)
    segmented = Image.fromarray(cells.repeat(tile_size, axis=0).repeat(tile_size, axis=1))
    # Step 5: Metrics
    mosaic_compare = mosaic.resize(img.size)
    mse_val = compute_mse(img, mosaic_compare)
    ssim_val = compute_ssim(img, mosaic_compare)
    runtime = time.time() - t0
    # Output: original, segmented (average grid), mosaic, metrics
    metrics = f"MSE: {mse_val:.2f}, SSIM: {ssim_val:.3f}, Time: {runtime:.2f} s"
    return img, segmented, mosaic, metrics

# Gradio interface setup
inputs = [
    gr.Image(type="pil", label="Input Image"),
    gr.Slider(8, 64, value=32, step=8, label="Grid Size"),
    gr.Slider(8, 32, value=16, step=4, label="Tile Size (px)"),
    gr.Slider(2, 4, value=3, step=1, label="Num Colors (per channel)")
]

outputs = [
    gr.Image(label="Original"),
    gr.Image(label="Segmented (Average Grid)"),
    gr.Image(label="Mosaic"),
    gr.Text(label="Metrics (MSE, SSIM, Timing)")
]

demo = gr.Interface(
    fn=mosaicify_vectorized,
    inputs=inputs,
    outputs=outputs,
    examples=get_example_images(),
    title="Mosaic Generator with Image Grid and Tiles",
    description=(
        "Upload or select a test image. Adjust the grid size, tile size, and color bucket count. "
        "The app divides your image, classifies color, and reconstructs a mosaic. "
        "Shows the original, the segmented-mean-color grid, and the final tile mosaic "
        "along with image similarity and runtime metrics."
    ),
    allow_flagging="never"
)

if __name__ == "__main__":
    demo.launch(share=True)
