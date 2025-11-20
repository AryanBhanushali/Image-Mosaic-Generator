import numpy as np
from skimage.metrics import mean_squared_error, structural_similarity as ssim

def compute_mse(img1, img2):
    """
    Compute mean squared error (MSE) between two images (PIL or array).
    """
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    return mean_squared_error(arr1, arr2)

def compute_ssim(img1, img2):
    """
    Compute structural similarity index (SSIM) between two images (PIL or array).
    """
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    return ssim(arr1, arr2, channel_axis=2)
