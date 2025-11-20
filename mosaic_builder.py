import numpy as np
from PIL import Image

def reconstruct_image_vectorized(classified_cells, tiles, colors, tile_size):
    """
    Reconstruct the output mosaic image from classified cell indices and prebuilt color tiles.
    Parameters:
        classified_cells (np.ndarray): (grid_size, grid_size, 3) array of color bucket indices (from classify_cells).
        tiles (List[np.ndarray]): List of all tile arrays as (tile_size, tile_size, 3).
        colors (np.ndarray): 1D array of bucket center RGB values.
        tile_size (int): Size in pixels of each tile's width/height.
    Returns:
        PIL.Image.Image: Final mosaic image assembled from the tiles to the appropriate size.
    """
    grid_size = classified_cells.shape[0]
    color_n = len(colors)
    idxs = (classified_cells[..., 0] * (color_n ** 2) +
            classified_cells[..., 1] * color_n +
            classified_cells[..., 2])
    tiles_array = np.stack(tiles, axis=0)  # shape: (num_tiles, tile_size, tile_size, 3)
    mosaic_tiles = tiles_array[idxs]  # shape: (grid_size, grid_size, tile_size, tile_size, 3)
    out_img = mosaic_tiles.transpose(0,2,1,3,4).reshape(grid_size*tile_size, grid_size*tile_size, 3)
    return Image.fromarray(out_img)