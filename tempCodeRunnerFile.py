if __name__ == "__main__":
    filepath = './dataset/testing/patient01-seg.nii.gz'  
    data = load_and_normalize_nifti(filepath)
    visualize_3d_volume(data, threshold=0.1)