from pathlib import Path

def scan_directory(directory_path):
    """
    Recursively scans the specified directory and lists all files.
    
    :param directory_path: The path of the directory to scan.
    :return: A list of file paths.
    """
    try:
        file_paths = [str(path) for path in Path(directory_path).rglob('*') if path.is_file()]
        return file_paths
    except PermissionError as e:
        print(f"Permission denied: {e}")
        return []
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return []
    except OSError as e:
        print(f"OS error: {e}")
        return []