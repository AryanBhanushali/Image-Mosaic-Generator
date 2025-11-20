import numpy as np

def build_tile_set(tile_size, n_colors):
    """
    Generate all colored square tiles for the mosaic, covering all possible RGB bucket combinations.
    Parameters:
        tile_size (int): Size (width/height) in pixels of each square tile.
        n_colors (int): Number of color buckets per RGB channel.
    Returns:
        tuple: (tiles, colors)
            - tiles (List[np.ndarray]): All (tile_size, tile_size, 3) tile arrays (one for each color combo)
            - colors (np.ndarray): Array of all bucket center values per channel.
    """
    colors = np.linspace(0, 255, n_colors, dtype=np.uint8)
    tiles = []
    for r in colors:
        for g in colors:
            for b in colors:
                tile = np.full((tile_size, tile_size, 3), (r, g, b), dtype=np.uint8)
                tiles.append(tile)
    return tiles, colors