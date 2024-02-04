# SummarizeTree

SummarizeTree is a Python application designed to traverse a directory structure on your local computer, analyze each file, and generate concise summaries using OpenAI's GPT models. This tool provides a high-level overview of a project's contents, aiding developers, managers, and other stakeholders in quickly understanding the purpose and functionality of various files within a project.

## Features

- Directory traversal and file identification
- File content analysis and summarization
- In-memory caching for efficient processing
- Progress tracking with visual feedback
- Command-line interface for ease of use
- Output summaries in a structured tree-like diagram

## Getting Started

### Prerequisites

- Python 3.8 or newer
- Virtual environment (recommended)

### Installation

1. Clone the repository to your local machine.
2. Navigate to the cloned directory and create a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with your OpenAI API key:

   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

### Usage

To use SummarizeTree, run the `analyze.py` script with the directory you wish to analyze:

```
python analyze.py /path/to/directory
```

The application will traverse the directory, analyze the files, and display a progress bar. Once completed, you will be presented with the summaries for review.

## Configuration

- `OPENAI_API_KEY`: Your OpenAI API key, used for authenticating with the GPT models.

## Modules

- `directory_scanner.py`: Handles directory traversal.
- `file_analyzer.py`: Reads and chunks file contents.
- `summary_generator.py`: Generates summaries using the OpenAI API.
- `analyze.py`: The main script that ties everything together.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

SummarizeTree is released under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- OpenAI for providing the GPT models used for summarization.
- The Python community for the libraries and tools that make this project possible.

## Contact

For support or queries, please open an issue on the GitHub repository page.

## Disclaimer

This tool is not affiliated with OpenAI. Please use responsibly and in accordance with OpenAI's usage policies.