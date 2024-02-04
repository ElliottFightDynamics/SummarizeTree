```python
def read_and_chunk_file(file_path, chunk_size=1000):
    """
    Reads the content of a file and splits it into manageable chunks.
    This is useful for processing large files that need to be summarized.

    :param file_path: The path to the file to be read and chunked.
    :param chunk_size: The size of each chunk in characters.
    :return: A list of text chunks.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
            return chunks
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while processing file {file_path}: {e}")
        return []
```