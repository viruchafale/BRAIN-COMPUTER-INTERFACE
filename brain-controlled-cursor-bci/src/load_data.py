import scipy.io

def load_mat_file(file_path):
    """
    Load a .mat file using scipy.io.loadmat.

    Args:
        file_path (str): Path to the .mat file.

    Returns:
        dict: Dictionary containing the data from the .mat file.
    """
    try:
        data = scipy.io.loadmat(file_path)
        return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None