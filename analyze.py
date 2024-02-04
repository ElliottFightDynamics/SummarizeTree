```python
import argparse
from directory_scanner import scan_directory
from file_analyzer import read_and_chunk_file
from summary_generator import generate_summary
from tqdm import tqdm
from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="SummarizeTree: Directory summarization tool")
    parser.add_argument("directory", help="Directory path to analyze and summarize")
    args = parser.parse_args()

    file_paths = scan_directory(args.directory)
    summaries_cache = {}

    for file_path in tqdm(file_paths, desc="Summarizing files"):
        if file_path not in summaries_cache:  # Check cache first
            chunks = read_and_chunk_file(file_path)
            summaries = [generate_summary(chunk) for chunk in chunks]
            summaries_cache[file_path] = " ".join(summaries)

    # Output summaries to console or file
    for file_path, summary in summaries_cache.items():
        print(f"File: {file_path}\nSummary: {summary}\n")

    # User confirmation step (optional implementation)
    # input("Press Enter to confirm the summaries...")

if __name__ == "__main__":
    main()
```