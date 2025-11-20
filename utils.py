import os
import glob
from mosaic_generator.config import DATASET_PATH

def get_example_images(n=2):
    """
    Retrieve file paths for sample images from the dataset directory, suitable for Gradio examples.
    Parameters:
        n (int): Number of sample image triplets to return.
    Returns:
        list: List of [filepath, grid_size, tile_size, n_colors] groups for app examples.
    """
    files = []
    exts = (".jpg", ".jpeg", ".png", ".bmp")
    for file in glob.glob(os.path.join(DATASET_PATH, "*")):
        if file.lower().endswith(exts):
            files.append(file)
        if len(files) >= n:
            break
    return [[f, 32, 16, 3] for f in files]
