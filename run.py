import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# load & normalisasi
def load_and_normalize_nifti(filepath):
    img = nib.load(filepath)
    data = img.get_fdata()
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized_data

# visualisasi 3D volume
def visualize_3d_volume(data, threshold=0.1):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    mask = data > threshold

    x, y, z = np.indices(data.shape)

    ax.scatter(x[mask], y[mask], z[mask], alpha=0.1, s=1)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# main
if __name__ == "__main__":
    filepath = './dataset/testing/patient03-seg.nii'  
    data = load_and_normalize_nifti(filepath)
    visualize_3d_volume(data, threshold=0.1)

    # filepath = './dataset/testing/patient01-seg.nii.gz'  