# PDF to Markdown Utility

This project provides a utility to convert PDF files into JPEG images and then convert those images into markdown format using OpenAI's API. It consists of several Python scripts, each serving a specific function in the conversion process.

## Prerequisites

- Python 3.x
- Virtual environment (optional but recommended)
- Required Python packages listed in `requirements.txt`

## Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY="your_actual_api_key_here"
   ```

## Usage

### Main Script

- **`main.py`**: This is the entry point of the application. It coordinates the conversion of a PDF file into images and then processes those images into markdown format.

  - **Functions**:
    - `main()`: Calls the `pdf_to_images` function to convert the PDF into images and then calls `process_images_to_markdown` to convert those images into markdown files.

### Image Splitter

- **`image_splitter.py`**: Handles the conversion of PDF files into individual JPEG images.

  - **Functions**:
    - `pdf_to_images(pdf_path, dpi=300, output_folder="page_jpegs")`: Converts each page of a PDF into a JPEG image and saves them in the specified output folder.

### Image to Markdown Converter

- **`image_to_markdowns.py`**: Converts the images into markdown format using OpenAI's API.

  - **Functions**:
    - `encode_image_to_base64(image_path)`: Encodes an image file to a base64 string.
    - `image_to_markdown(base64_image)`: Sends a base64-encoded image to the OpenAI API to get a markdown description.
    - `process_images_to_markdown(image_folder="page_jpegs", output_folder="page_markdowns")`: Processes all images in a specified folder, converting them to markdown using the `image_to_markdown` function.

## Notes

- Ensure your `.env` file is correctly set up with your OpenAI API key.
- The output markdown files are saved in the `page_markdowns` directory.

## License

This project is licensed under the MIT License.
