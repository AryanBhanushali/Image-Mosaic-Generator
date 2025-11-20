import numpy as np
import os
import glob
from PIL import Image
from mosaic_generator.config import DATASET_PATH

# Resize/crop image to multiples of grid_size
def preprocess_image(img, grid_size):
    """
    Convert the image to RGB, and crop so its width and height are multiples of grid_size.
    Parameters:
        img (PIL.Image.Image): The input image object.
        grid_size (int): Number of grid cells along each dimension.
    Returns:
        PIL.Image.Image: Cropped RGB image compatible with grid division.
    """
    img = img.convert('RGB')
    w, h = img.size
    new_w = (w // grid_size) * grid_size
    new_h = (h // grid_size) * grid_size
    img = img.crop((0, 0, new_w, new_h))
    return img

# Divide image into grid, return average color per cell as 3D array (grid,grid,3)
def image_to_grid(img, grid_size):
    """
    Divide an image into a grid and compute the average color for each cell.
    Parameters:
        img (PIL.Image.Image): The cropped input image.
        grid_size (int): Number of grid cells along each dimension.
    Returns:
        np.ndarray: (grid_size, grid_size, 3) array with mean RGB color per cell.
    """
    img_np = np.array(img)
    h, w, c = img_np.shape
    tile_h = h // grid_size
    tile_w = w // grid_size
    # Reshape and average
    grid_cells = img_np.reshape(grid_size, tile_h, grid_size, tile_w, c).mean(axis=(1,3)).astype(np.uint8)
    return grid_cells

# Quantize each cell to nearest color bucket (per channel)
def classify_cells(cells, n_colors):
    """
    Quantize each cell in the grid to its nearest color bucket in each channel.
    Parameters:
        cells (np.ndarray): (grid_size, grid_size, 3) array of mean RGB cell colors.
        n_colors (int): Number of color buckets per channel (between 2–4 typically).
    Returns:
        np.ndarray: (grid_size, grid_size, 3) array of integer color bucket indices.
    """
    bins = np.linspace(0, 255, n_colors+1, dtype=np.uint8)
    quantized = np.digitize(cells, bins) - 1
    return quantized